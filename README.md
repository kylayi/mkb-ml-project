# Segmentasi Pelanggan UMKM Roti & Kopi · Tim [nama tim]

**Kasus:** 05 · Segmentasi pelanggan UMKM · **Aplikasi:** [tautan Streamlit] · **Video:** [tautan video]

| Anggota | NIM | Bagian yang dikerjakan |
|---|---|---|
| [nama] | [NIM] | [misalnya EDA dan pembersihan data] |
| [nama] | [NIM] | [misalnya model dan evaluasi] |
| [nama] | [NIM] | [misalnya API dan aplikasi] |

## Masalah dan pengguna

Pemilik UMKM roti dan kopi di Bandung punya ±10.000 anggota aplikasi member, tetapi selama ini mengirim promo
yang sama ke semua orang. Model ini mengelompokkan anggota menjadi 4 tipe pelanggan berdasarkan perilaku
belanjanya, lalu menyarankan satu promo yang cocok untuk tiap tipe. Aplikasinya menerima data satu pelanggan
(atau file CSV) dan menampilkan segmen serta promo yang disarankan.

## Data dan pembersihan

Sumber: [`kasus/05-segmentasi-umkm/data/raw.csv`](kasus/05-segmentasi-umkm/data/raw.csv), 10.150 baris, 12 kolom.

| Masalah yang ditemukan | Jumlah baris | Cara menangani |
|---|---|---|
| ID pelanggan ganda (90 duplikat persis + 60 hanya beda recency 1 hari) | 150 | simpan 1 baris per ID, ambil recency terkecil (ekspor terbaru) |
| `total_belanja_rp` berformat teks `Rp 1.044.300` | 507 | hapus `Rp` dan titik ribuan, ubah ke angka |
| Penulisan kecamatan tidak baku (`SUKAJADI`, `coblong`, `Buah Batu`, `Bdg Wetan`, spasi di belakang) | 254 | dipetakan ke 10 nama baku |
| Umur mustahil (0, 1, 99, 120) | 100 | dikosongkan lalu diisi median; umur hanya untuk profil |
| Umur kosong | 208 | diisi median |
| Rating kosong | 800 | ditandai `pernah_rating`; rating hanya untuk profil |
| Transaksi terakhir sebelum tanggal daftar | 283 | ditandai, tidak dihapus (`tanggal_daftar` tidak dipakai model) |
| Recency > 180 hari padahal data 6 bulan | 64 | dipotong ke 180 saat membuat fitur |

Hasil akhir: 10.000 pelanggan unik.

## Fitur dan model

Fitur clustering hanya memakai perilaku belanja (lihat [`src/features.py`](src/features.py)):
`log(recency)`, `log(jumlah transaksi)`, `log(belanja per transaksi)`, dan `persen pakai promo`, lalu
StandardScaler. Variabel kategorikal (channel, kategori favorit, kecamatan, metode bayar), umur, dan rating
dipakai untuk membaca profil segmen, bukan untuk clustering.

## Hasil

| Model | Silhouette | Davies-Bouldin |
|---|---|---|
| *Baseline*: K-Means pada RFM mentah (k terbaik = 4) | 0,554 | 0,64 |
| **Final: K-Means k = 4 pada fitur log + basket + promo** | **0,613** | **0,55** |
| Pembanding: Gaussian Mixture, k = 4 | 0,611 | 0,55 |
| Pembanding: Agglomerative Ward, k = 4 (sampel 4.000) | 0,612 | 0,54 |

Alasan memilih **k = 4**: silhouette tertinggi dan Davies-Bouldin terendah, elbow menekuk di k = 4, hasil stabil
(ARI = 1,00 antar-seed dan antar-subsampel 80%), dan k = 5 hanya memecah pelanggan setia menjadi dua kelompok
yang tidak membutuhkan promo berbeda. 88% pelanggan memiliki silhouette > 0,5.

Tidak ada *threshold* klasifikasi. Penggantinya adalah **ambang jarak** (persentil-99 jarak ke pusat segmen,
1,84): pelanggan di atas ambang ini tetap diberi segmen terdekat, tetapi ditandai "di luar kebiasaan".

| Segmen | Porsi anggota | Porsi omzet | Ciri (median) | Promo yang disarankan |
|---|---|---|---|---|
| Pelanggan Setia | 30% | 58% | 28 transaksi, 5 hari lalu, promo 20%, 68% di toko | program poin / tier, hadiah non-diskon |
| Pemburu Promo Online | 25% | 12% | 11 transaksi, promo 82%, basket terkecil, dominan ojol | bundling dengan minimum belanja + voucher ambil di toko |
| Pembeli Momen Spesial | 15% | 24% | 4 transaksi, ±Rp 276 ribu/transaksi, kue ulang tahun & snack box | pengingat acara + pre-order + bonus layanan |
| Mulai Menghilang | 30% | 5% | 110 hari tidak datang, rating terendah (3,6) | voucher win-back berbatas waktu + survei perbaikan |

## Cara menjalankan

```bash
pip install -r requirements.txt
streamlit run app/ui/streamlit_app.py   # aplikasi
uvicorn app.api.main:app --reload       # API (opsional), dokumentasi di /docs
pip install -r requirements-dev.txt
pytest                                  # smoke test API: normal, ekstrem, tidak valid
```

Melatih ulang model: jalankan [`notebooks/01_segmentasi_pelanggan.ipynb`](notebooks/01_segmentasi_pelanggan.ipynb)
dari awal sampai akhir; notebook menulis ulang `artifacts/model.joblib` dan `artifacts/metadata.json`.

## Struktur repositori

```
kasus/05-segmentasi-umkm/  brief dan data mentah dari klien
notebooks/                 notebook dari audit data sampai penyimpanan model
data/                      data tersegmentasi + contoh CSV untuk aplikasi
src/features.py            pembersihan dan pembuat fitur, dipakai saat pelatihan dan saat prediksi
src/segmen.py              nama, profil, dan promo setiap segmen
artifacts/                 model.joblib + metadata.json
app/predictor.py           load model, validasi masukan, prediksi
app/ui/streamlit_app.py    aplikasi untuk pemilik UMKM
app/api/main.py            FastAPI
tests/                     smoke test API
```

## Keterbatasan

- Segmen adalah potret data 6 bulan sampai Juni 2026; pelanggan bisa berpindah segmen, jadi model perlu dilatih
  ulang berkala (misalnya tiap bulan).
- Data bersifat sintetis dan pemisahan segmennya sangat jelas; pada data toko sungguhan skor silhouette
  kemungkinan lebih rendah.
- Ketepatan rekomendasi promo belum terbukti. Perlu A/B test per segmen (promo khusus segmen vs promo biasa).
- 283 tanggal daftar tidak konsisten dengan recency dan perlu dikonfirmasi ke klien.
- Pelanggan yang belum pernah bertransaksi (0 transaksi) belum bisa disegmentasi.

## Daftar periksa sebelum dikumpulkan

- [ ] Repositori bersifat publik dan setiap anggota memiliki *commit*
- [x] *Notebook* dapat dijalankan ulang dari awal sampai akhir tanpa galat
- [x] *Baseline* wajib dilaporkan dan dibandingkan
- [x] `artifacts/metadata.json` berisi versi model, fitur masukan, ambang, dan metrik
- [ ] Aplikasi dapat dibuka orang lain melalui tautan, termasuk dari ponsel
- [x] Aplikasi tidak berhenti mendadak ketika menerima masukan yang tidak wajar
- [ ] Laporan paling banyak 6 halaman dan video paling lama 5 menit
