"""Pembersihan data dan pembuatan fitur.

Dipakai notebook pelatihan dan aplikasi (app/predictor.py), jadi praprosesnya selalu sama.
model.joblib menyimpan referensi ke src.features.PembuatFitur: jangan pindahkan kelas ini tanpa melatih ulang.
"""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# Data mencakup 6 bulan sampai akhir Juni 2026.
TANGGAL_REFERENSI = pd.Timestamp("2026-06-30")
BATAS_RECENCY = 180  # jendela data 6 bulan
UMUR_MIN, UMUR_MAX = 15, 80

KOLOM_INPUT = [
    "jumlah_transaksi_6bln",
    "total_belanja_rp",
    "hari_sejak_transaksi_terakhir",
    "persen_pakai_promo",
]
FITUR_MODEL = ["recency_log", "frekuensi_log", "basket_log", "persen_pakai_promo"]

PETA_KECAMATAN = {
    "sukajadi": "Sukajadi",
    "coblong": "Coblong",
    "buah batu": "Buahbatu",
    "buahbatu": "Buahbatu",
    "bdg wetan": "Bandung Wetan",
    "bandung wetan": "Bandung Wetan",
    "cibeunying kidul": "Cibeunying Kidul",
    "cidadap": "Cidadap",
    "sumur bandung": "Sumur Bandung",
    "arcamanik": "Arcamanik",
    "lengkong": "Lengkong",
    "antapani": "Antapani",
}


def parse_rupiah(nilai):
    """Ubah '1791100', 1791100, atau 'Rp 1.044.300' menjadi float."""
    if nilai is None or (isinstance(nilai, float) and np.isnan(nilai)):
        return np.nan
    if isinstance(nilai, (int, float, np.number)):
        return float(nilai)
    teks = str(nilai).replace("Rp", "").replace("rp", "").replace(".", "").replace(",", "").strip()
    return float(teks) if teks else np.nan


def bersihkan(df):
    """Pembersihan dataset mentah. Mengembalikan (df_bersih, log_langkah)."""
    log = {}
    df = df.copy()
    log["baris_awal"] = len(df)

    df["total_belanja_rp"] = df["total_belanja_rp"].map(parse_rupiah)

    kec = df["kecamatan"].str.strip().str.lower()
    log["kecamatan_dirapikan"] = int((df["kecamatan"] != kec.map(PETA_KECAMATAN)).sum())
    df["kecamatan"] = kec.map(PETA_KECAMATAN).fillna(df["kecamatan"].str.strip())

    # ID ganda: duplikat persis, atau versi yang hanya beda recency 1 hari (diekspor di hari berbeda).
    # Simpan yang recency-nya paling kecil (data paling baru).
    log["duplikat_persis"] = int(df.duplicated().sum())
    df = df.sort_values("hari_sejak_transaksi_terakhir").drop_duplicates("id_pelanggan", keep="first")
    log["baris_setelah_dedup"] = len(df)

    umur_aneh = (df["umur"] < UMUR_MIN) | (df["umur"] > UMUR_MAX)
    log["umur_tidak_wajar"] = int(umur_aneh.sum())
    df.loc[umur_aneh, "umur"] = np.nan
    log["umur_kosong"] = int(df["umur"].isna().sum())
    df["umur"] = df["umur"].fillna(df["umur"].median())

    df["pernah_rating"] = df["rating_rata"].notna()
    log["rating_kosong"] = int((~df["pernah_rating"]).sum())

    df["tanggal_daftar"] = pd.to_datetime(df["tanggal_daftar"])
    df["masa_member_hari"] = (TANGGAL_REFERENSI - df["tanggal_daftar"]).dt.days
    df["flag_recency_gt_masa_member"] = df["hari_sejak_transaksi_terakhir"] > df["masa_member_hari"]
    log["recency_lebih_dari_masa_member"] = int(df["flag_recency_gt_masa_member"].sum())
    log["recency_lebih_dari_180"] = int((df["hari_sejak_transaksi_terakhir"] > BATAS_RECENCY).sum())

    log["baris_akhir"] = len(df)
    return df.sort_values("id_pelanggan").reset_index(drop=True), log


class PembuatFitur(BaseEstimator, TransformerMixin):
    """Fitur perilaku untuk clustering: recency, frekuensi, nilai per transaksi (basket), promo.

    Recency, frekuensi, dan basket di-log agar outlier tidak mendominasi jarak K-Means.
    Total belanja tidak dipakai langsung karena = frekuensi x basket (redundan).
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X, columns=KOLOM_INPUT).copy()
        X["total_belanja_rp"] = X["total_belanja_rp"].map(parse_rupiah)
        trx = X["jumlah_transaksi_6bln"].astype(float).clip(lower=1)
        recency = X["hari_sejak_transaksi_terakhir"].astype(float).clip(0, BATAS_RECENCY)
        basket = X["total_belanja_rp"] / trx
        return pd.DataFrame({
            "recency_log": np.log1p(recency),
            "frekuensi_log": np.log1p(trx),
            "basket_log": np.log1p(basket),
            "persen_pakai_promo": X["persen_pakai_promo"].astype(float).clip(0, 100),
        }, index=X.index)

    def get_feature_names_out(self, input_features=None):
        return np.array(FITUR_MODEL)
