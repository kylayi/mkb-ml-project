"""UI Streamlit untuk pemilik UMKM roti & kopi: data satu pelanggan masuk, segmen + promo keluar.

Jalankan dari root repo:
    streamlit run app/ui/streamlit_app.py

Dua mode:
- Mode A (API_URL kosong): model di-load langsung di sini. Paling gampang di-deploy.
- Mode B (API_URL diisi): memanggil FastAPI lewat HTTP.
  Isi lewat environment variable API_URL, atau di Streamlit Cloud: Settings → Secrets → API_URL = "https://..."
"""
import os
import sys
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))  # Streamlit menjalankan file ini dari app/ui, jadi root repo ditambah manual
from app import predictor  # noqa: E402


def _api_url() -> str:
    try:
        url = st.secrets.get("API_URL", "")
    except Exception:  # tidak ada secrets.toml: wajar saat lokal
        url = ""
    return (url or os.getenv("API_URL", "")).rstrip("/")


API_URL = _api_url()
TIMEOUT = 60  # detik; free tier yang sedang tidur butuh waktu untuk bangun


def prediksi(rows: list[dict]) -> list[dict]:
    """Baris sudah divalidasi sebelum masuk sini."""
    if not API_URL:
        return predictor.predict_rows(rows)
    path = "/predict" if len(rows) == 1 else "/predict/batch"
    r = requests.post(API_URL + path, json=rows[0] if len(rows) == 1 else rows, timeout=TIMEOUT)
    if r.status_code == 422:
        raise ValueError(f"Input ditolak API (422): {r.json().get('detail')}")
    r.raise_for_status()
    hasil = r.json()
    return [hasil] if len(rows) == 1 else hasil


def rupiah(x: float) -> str:
    return "Rp " + f"{x:,.0f}".replace(",", ".")


st.set_page_config(page_title="Segmentasi Pelanggan Roti & Kopi", page_icon="☕", layout="centered")
st.title("Segmentasi pelanggan")
st.caption("Masukkan data belanja satu anggota, lihat dia termasuk tipe pelanggan apa dan promo apa yang cocok.")

try:
    _, META = predictor.load()
except Exception as e:
    st.error(f"Model belum siap: {e}")
    st.stop()

FITUR = META["fitur_input"]
SEGMEN = META["segmen"]
mode = f"Mode B · memanggil API {API_URL}" if API_URL else "Mode A · model di-load langsung"
st.info(f"{mode} · versi model {META['versi_model']} · {META['k']} segmen")

tab_satu, tab_batch, tab_info = st.tabs(["Satu pelanggan", "Banyak pelanggan (CSV)", "Tentang segmen"])

with tab_satu:
    with st.form("input"):
        c1, c2 = st.columns(2)
        trx = c1.number_input("Jumlah transaksi 6 bulan terakhir", min_value=0, max_value=1000, value=12, step=1,
                              key="trx")
        belanja = c2.number_input("Total belanja 6 bulan (Rp)", min_value=0, max_value=200_000_000,
                                  value=420_000, step=10_000, key="belanja")
        hari = c1.number_input("Hari sejak transaksi terakhir", min_value=0, max_value=1000, value=9, step=1,
                               key="hari")
        promo = c2.number_input("Persen transaksi yang memakai promo (%)", min_value=0, max_value=100,
                                value=85, step=1, key="promo")
        kirim = st.form_submit_button("Cek segmen", type="primary", use_container_width=True)

    if kirim:
        row = {"jumlah_transaksi_6bln": int(trx), "total_belanja_rp": float(belanja),
               "hari_sejak_transaksi_terakhir": int(hari), "persen_pakai_promo": float(promo)}
        galat = predictor.validasi(row)
        if galat:
            st.error("Data belum bisa diproses:\n\n" + "\n".join(f"- {g}" for g in galat))
        else:
            try:
                hasil = prediksi([row])[0]
            except Exception as e:
                st.error(f"Gagal memprediksi: {e}")
            else:
                nama = hasil["segmen"]
                with st.container(border=True):
                    st.markdown(f"#### Segmen: {nama}")
                    st.write(hasil["profil"])
                    st.markdown(f"**Promo yang disarankan:** {hasil['promo_disarankan']}")
                for c in hasil["catatan"]:
                    st.warning(c)

                med = SEGMEN[nama]["median"]
                st.markdown(f"**Pelanggan ini dibandingkan dengan median segmen {nama}**")
                banding = pd.DataFrame({
                    "": ["Transaksi 6 bln", "Belanja per transaksi", "Hari sejak transaksi terakhir", "Pakai promo"],
                    "Pelanggan ini": [f"{trx}x", rupiah(belanja / trx), f"{hari} hari", f"{promo}%"],
                    "Median segmen": [f"{med['transaksi_6bln']:.0f}x", rupiah(med["basket"]),
                                      f"{med['recency_hari']:.0f} hari", f"{med['promo_pct']:.0f}%"],
                })
                st.dataframe(banding, hide_index=True, use_container_width=True)
                with st.expander("Lihat request & response JSON"):
                    st.json({"request": row, "response": hasil})

with tab_batch:
    st.write("Upload CSV dengan kolom: " + ", ".join(f"`{k}`" for k in FITUR)
             + ". Kolom lain (misalnya `id_pelanggan`) ikut ditampilkan.")
    contoh = ROOT / "data" / "contoh_batch.csv"
    if contoh.exists():
        st.download_button("Unduh contoh CSV", contoh.read_bytes(), "contoh_batch.csv", "text/csv")
    up = st.file_uploader("CSV", type="csv")
    if up is not None:
        try:
            df = pd.read_csv(up)
        except Exception as e:
            st.error(f"File tidak bisa dibaca sebagai CSV: {e}")
            st.stop()
        kurang = [k for k in FITUR if k not in df.columns]
        if kurang:
            st.error(f"Kolom kurang: {kurang}")
        elif df.empty:
            st.warning("File CSV kosong.")
        else:
            X = df[FITUR].astype(object).where(df[FITUR].notna(), None)
            rows = X.to_dict("records")
            alasan = [("; ".join(predictor.validasi(r)) or None) for r in rows]
            valid = [i for i, a in enumerate(alasan) if a is None]
            out = df.reset_index(drop=True).copy()
            out["segmen"] = "TIDAK VALID"
            out["promo_disarankan"] = ""
            out["keterangan"] = [a or "" for a in alasan]
            try:
                hasil = prediksi([rows[i] for i in valid]) if valid else []
            except Exception as e:
                st.error(f"Gagal memprediksi: {e}")
            else:
                for i, h in zip(valid, hasil):
                    out.loc[i, ["segmen", "promo_disarankan"]] = [h["segmen"], h["promo_disarankan"]]
                    out.loc[i, "keterangan"] = " ".join(h["catatan"])
                c1, c2 = st.columns(2)
                c1.metric("Pelanggan diproses", f"{len(valid)} dari {len(out)}")
                c2.metric("Baris tidak valid", len(out) - len(valid))
                jumlah = (out["segmen"].value_counts().rename_axis("segmen").reset_index(name="jumlah"))
                jumlah["porsi"] = jumlah["jumlah"] / len(out)
                st.dataframe(jumlah, hide_index=True, use_container_width=True, column_config={
                    "porsi": st.column_config.ProgressColumn("porsi", format="percent", min_value=0, max_value=1)})
                st.dataframe(out, use_container_width=True, hide_index=True)
                st.download_button("Unduh hasil", out.to_csv(index=False).encode(), "hasil_segmentasi.csv", "text/csv")

with tab_info:
    m = META["metrik"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Silhouette model", f"{m['silhouette_final']:.3f}",
              delta=f"{m['silhouette_final'] - m['silhouette_baseline_kmeans_rfm_mentah']:+.3f} vs baseline")
    c2.metric("Davies-Bouldin", f"{m['davies_bouldin_final']:.2f}", help="Semakin rendah semakin baik")
    c3.metric("Stabilitas (ARI)", f"{m['ari_stabilitas_subsampel_80']:.2f}", help="1 = hasil selalu sama")
    st.caption(f"Dilatih dengan {META['data_latih']['baris_akhir']:,} anggota (data 6 bulan sampai Juni 2026). "
               f"Algoritma: {META['algoritma']}.")
    for nama, info in SEGMEN.items():
        med = info["median"]
        with st.container(border=True):
            st.markdown(f"#### {nama}  ·  {med['porsi_%']:.0f}% anggota, {med['kontribusi_omzet_%']:.0f}% omzet")
            st.write(info["profil"])
            st.markdown(f"**Promo:** {info['promo']}")
            st.caption(f"Median: {med['transaksi_6bln']:.0f} transaksi · {rupiah(med['basket'])} per transaksi · "
                       f"{med['recency_hari']:.0f} hari sejak transaksi terakhir · promo {med['promo_pct']:.0f}%")
