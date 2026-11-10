"""Load artifact sekali, lalu prediksi segmen. Dipakai FastAPI (app/api/main.py) dan Streamlit mode A."""
import json
import sys
import time
from functools import lru_cache
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
# model.joblib menyimpan referensi ke src.features.PembuatFitur, jadi root repo harus bisa di-import
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.features import BATAS_RECENCY, parse_rupiah  # noqa: E402

ARTIFACT_DIR = ROOT / "artifacts"


@lru_cache(maxsize=1)
def load():
    """(model, metadata). lru_cache = di-load sekali per proses, bukan per request."""
    model_path, meta_path = ARTIFACT_DIR / "model.joblib", ARTIFACT_DIR / "metadata.json"
    if not model_path.exists():
        raise FileNotFoundError(f"{model_path} tidak ada. Sudah di-commit? Cek .gitignore.")
    model = joblib.load(model_path)
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    return model, meta


def _angka(x: float) -> str:
    """Format ribuan gaya Indonesia: 1000000 -> 1.000.000"""
    return f"{x:,.0f}".replace(",", ".")


def validasi(row: dict) -> list[str]:
    """Kembalikan daftar pesan galat. Kosong = masukan valid. Batas diambil dari metadata."""
    _, meta = load()
    batas = meta["batas_input"]
    galat = []
    nilai = {}
    for kolom in meta["fitur_input"]:
        v = row.get(kolom)
        if kolom == "total_belanja_rp":
            try:
                v = parse_rupiah(v)
            except ValueError:
                v = "bukan angka"
        try:
            v = float(v)
        except (TypeError, ValueError):
            galat.append(f"{kolom}: wajib diisi dengan angka (diterima: {row.get(kolom)!r})")
            continue
        if np.isnan(v):
            galat.append(f"{kolom}: wajib diisi")
            continue
        lo, hi = batas[kolom]
        if not lo <= v <= hi:
            galat.append(f"{kolom}: harus di antara {_angka(lo)} dan {_angka(hi)} (diterima: {_angka(v)})")
        nilai[kolom] = v
    if not galat:
        basket = nilai["total_belanja_rp"] / nilai["jumlah_transaksi_6bln"]
        lo, hi = batas["belanja_per_transaksi"]
        if not lo <= basket <= hi:
            galat.append(f"total belanja ÷ jumlah transaksi = Rp {_angka(basket)} per transaksi, tidak masuk akal "
                         f"(harus Rp {_angka(lo)} - Rp {_angka(hi)})")
    return galat


def predict_rows(rows: list[dict]) -> list[dict]:
    """Prediksi beberapa pelanggan sekaligus. Tiap baris berisi kolom fitur_input dari metadata.
    Baris tidak valid memunculkan ValueError dengan pesan yang bisa dibaca pemilik toko."""
    model, meta = load()
    for i, row in enumerate(rows):
        galat = validasi(row)
        if galat:
            awalan = f"Baris {i + 1}: " if len(rows) > 1 else ""
            raise ValueError(awalan + "; ".join(galat))

    mulai = time.perf_counter()
    X = pd.DataFrame(rows)[meta["fitur_input"]]
    label = model.predict(X)
    jarak = model.transform(X)  # jarak ke setiap pusat segmen
    latency = round((time.perf_counter() - mulai) * 1000, 1)

    hasil = []
    for row, lab, d in zip(rows, label, jarak):
        nama = meta["nama_cluster"][str(int(lab))]
        urut = np.sort(d)
        catatan = []
        if urut[0] > meta["ambang_jarak"]:
            catatan.append("Perilaku pelanggan ini jauh dari semua segmen; segmen di atas adalah yang paling mirip.")
        elif urut[0] / urut[1] > 0.8:
            catatan.append("Pelanggan ini berada di perbatasan dua segmen.")
        if float(row["hari_sejak_transaksi_terakhir"]) > BATAS_RECENCY:
            catatan.append(f"Hari sejak transaksi terakhir dihitung maksimal {BATAS_RECENCY} hari (jendela data 6 bulan).")
        hasil.append({
            "segmen": nama,
            "profil": meta["segmen"][nama]["profil"],
            "promo_disarankan": meta["segmen"][nama]["promo"],
            "jarak_ke_pusat": round(float(urut[0]), 3),
            "di_luar_kebiasaan": bool(urut[0] > meta["ambang_jarak"]),
            "catatan": catatan,
            "versi_model": meta["versi_model"],
            "latency_ms": latency,
        })
    return hasil


def predict_one(row: dict) -> dict:
    return predict_rows([row])[0]
