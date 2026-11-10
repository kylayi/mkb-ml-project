"""Smoke test API: input normal, ekstrem, dan tidak valid. Jalankan dari root repo: pytest -q"""
import pytest
from fastapi.testclient import TestClient

from app.api.main import app

NORMAL = {"jumlah_transaksi_6bln": 12, "total_belanja_rp": 420_000,
          "hari_sejak_transaksi_terakhir": 9, "persen_pakai_promo": 85}

CONTOH_SEGMEN = [
    ({"jumlah_transaksi_6bln": 32, "total_belanja_rp": 1_600_000, "hari_sejak_transaksi_terakhir": 3,
      "persen_pakai_promo": 15}, "Pelanggan Setia"),
    (NORMAL, "Pemburu Promo Online"),
    ({"jumlah_transaksi_6bln": 3, "total_belanja_rp": 1_250_000, "hari_sejak_transaksi_terakhir": 40,
      "persen_pakai_promo": 5}, "Pembeli Momen Spesial"),
    ({"jumlah_transaksi_6bln": 2, "total_belanja_rp": 70_000, "hari_sejak_transaksi_terakhir": 140,
      "persen_pakai_promo": 40}, "Mulai Menghilang"),
]


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:  # `with` menjalankan startup: model di-load sekali
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok" and r.json()["k"] == 4


@pytest.mark.parametrize("row,segmen", CONTOH_SEGMEN)
def test_setiap_segmen_tipikal(client, row, segmen):
    r = client.post("/predict", json=row)
    assert r.status_code == 200, r.text
    assert r.json()["segmen"] == segmen
    assert r.json()["di_luar_kebiasaan"] is False


def test_rupiah_berformat_teks_diterima(client):
    a = client.post("/predict", json={**NORMAL, "total_belanja_rp": "Rp 420.000"}).json()
    b = client.post("/predict", json=NORMAL).json()
    assert a["segmen"] == b["segmen"] and a["jarak_ke_pusat"] == b["jarak_ke_pusat"]


def test_ekstrem_tetap_dijawab_dan_ditandai(client):
    ekstrem = {"jumlah_transaksi_6bln": 500, "total_belanja_rp": 100_000_000,
               "hari_sejak_transaksi_terakhir": 0, "persen_pakai_promo": 0}
    r = client.post("/predict", json=ekstrem)
    assert r.status_code == 200
    assert r.json()["di_luar_kebiasaan"] is True


def test_recency_lebih_dari_6_bulan_diberi_catatan(client):
    r = client.post("/predict", json={**NORMAL, "hari_sejak_transaksi_terakhir": 300})
    assert r.status_code == 200
    assert any("maksimal" in c for c in r.json()["catatan"])


@pytest.mark.parametrize("field,value", [
    ("jumlah_transaksi_6bln", 0), ("jumlah_transaksi_6bln", -3), ("total_belanja_rp", -1),
    ("total_belanja_rp", "abc"), ("hari_sejak_transaksi_terakhir", 400), ("persen_pakai_promo", 150),
    ("persen_pakai_promo", "banyak"),
])
def test_tidak_valid_ditolak_422(client, field, value):
    r = client.post("/predict", json={**NORMAL, field: value})
    assert r.status_code == 422
    assert r.json()["detail"][0]["loc"][-1] == field


def test_belanja_per_transaksi_mustahil_ditolak(client):
    r = client.post("/predict", json={**NORMAL, "jumlah_transaksi_6bln": 50, "total_belanja_rp": 10_000})
    assert r.status_code == 422


def test_kolom_kurang_ditolak(client):
    body = {k: v for k, v in NORMAL.items() if k != "persen_pakai_promo"}
    assert client.post("/predict", json=body).status_code == 422


def test_batch(client):
    r = client.post("/predict/batch", json=[row for row, _ in CONTOH_SEGMEN])
    assert r.status_code == 200
    assert [h["segmen"] for h in r.json()] == [s for _, s in CONTOH_SEGMEN]
    assert client.post("/predict/batch", json=[]).json() == []
