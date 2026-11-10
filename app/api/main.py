"""FastAPI untuk model segmentasi pelanggan UMKM roti & kopi.

Jalankan dari root repo:
    uvicorn app.api.main:app --reload
Lalu buka http://127.0.0.1:8000/docs
"""
import json
import logging
import sys
import time
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator, model_validator

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # supaya `app` dan `src` bisa di-import
from app import predictor  # noqa: E402
from src.features import parse_rupiah  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("segmentasi")

MAX_BATCH = 1000


@asynccontextmanager
async def lifespan(app: FastAPI):
    predictor.load()  # load sekali saat startup, bukan per request
    yield


app = FastAPI(title="Segmentasi Pelanggan UMKM Roti & Kopi", version="1.0.0", lifespan=lifespan)


class InputData(BaseModel):
    """Validasi: nilai mustahil ditolak 422 sebelum menyentuh model. Batas sama dengan metadata.json."""
    jumlah_transaksi_6bln: int = Field(ge=1, le=500)
    total_belanja_rp: float = Field(ge=1_000, le=100_000_000, description="Angka atau teks 'Rp 1.044.300'")
    hari_sejak_transaksi_terakhir: int = Field(ge=0, le=365)
    persen_pakai_promo: float = Field(ge=0, le=100)

    @field_validator("total_belanja_rp", mode="before")
    @classmethod
    def rapikan_rupiah(cls, v):
        return parse_rupiah(v) if isinstance(v, str) else v

    @model_validator(mode="after")
    def belanja_per_transaksi_masuk_akal(self):
        basket = self.total_belanja_rp / self.jumlah_transaksi_6bln
        if not 1_000 <= basket <= 5_000_000:
            raise ValueError(f"belanja per transaksi Rp {basket:,.0f} tidak masuk akal (Rp 1.000 - Rp 5.000.000)"
                             .replace(",", "."))
        return self

    model_config = {"json_schema_extra": {"examples": [{
        "jumlah_transaksi_6bln": 12, "total_belanja_rp": "Rp 420.000",
        "hari_sejak_transaksi_terakhir": 9, "persen_pakai_promo": 85}]}}


class Prediksi(BaseModel):
    segmen: str
    profil: str
    promo_disarankan: str
    jarak_ke_pusat: float
    di_luar_kebiasaan: bool
    catatan: list[str]
    versi_model: str
    latency_ms: float


def _log(inputs: list[dict], outputs: list[dict]):
    """Setiap prediksi di-log: input + output, supaya bisa diaudit dan dipantau pergeseran datanya."""
    for x, y in zip(inputs, outputs):
        log.info("prediksi %s", json.dumps({"input": x, "segmen": y["segmen"], "ts": time.time()}))


@app.get("/health")
def health():
    _, meta = predictor.load()
    return {"status": "ok", "versi_model": meta["versi_model"], "k": meta["k"],
            "fitur_input": meta["fitur_input"], "segmen": list(meta["segmen"])}


@app.post("/predict", response_model=Prediksi)
def predict(x: InputData):
    row = x.model_dump()
    hasil = predictor.predict_one(row)
    _log([row], [hasil])
    return hasil


@app.post("/predict/batch", response_model=list[Prediksi])
def predict_batch(xs: list[InputData]):
    if len(xs) > MAX_BATCH:
        raise HTTPException(413, f"Maksimal {MAX_BATCH} baris per request.")
    rows = [x.model_dump() for x in xs]
    if not rows:
        return []
    hasil = predictor.predict_rows(rows)
    _log(rows, hasil)
    return hasil
