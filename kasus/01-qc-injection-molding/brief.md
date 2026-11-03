# Kasus 01 · Quality control injection molding

**Klien:** kepala QC pabrik komponen plastik (tutup botol, housing, klip) di Cikarang.

> *"Part cacat baru ketahuan waktu inspeksi visual di akhir shift. Kalau mesin bisa ngasih tahu dari
> parameter prosesnya bahwa part ini kemungkinan cacat, part itu bisa langsung dipisahin dan settingan
> mesinnya dibetulkan sebelum ratusan part lain ikut cacat."*

## Yang diminta

Model yang menerima parameter satu siklus cetak dan menjawab: **part ini cacat atau tidak**, lengkap dengan
probabilitasnya.

## Data

`data/injection_molding.csv`: satu baris = satu siklus cetak (satu part), 4 mesin, Maret–Juni 2026.

| Kolom | Arti |
|---|---|
| `waktu_produksi` | waktu siklus |
| `mesin` | IM-01 sampai IM-04 |
| `shift` | pagi, siang, malam |
| `bahan` | PP, ABS, atau PC |
| `suhu_leleh_C` | suhu plastik leleh di barrel (°C) |
| `suhu_cetakan_C` | suhu cetakan (°C) |
| `tekanan_injeksi_bar` | tekanan injeksi (bar) |
| `kecepatan_injeksi_mm_s` | kecepatan dorong screw (mm/s) |
| `waktu_pendinginan_s` | lama part didinginkan di cetakan (detik) |
| `waktu_siklus_s` | lama satu siklus penuh (detik) |
| `kelembaban_bahan_pct` | kadar air bahan sebelum dicetak (%) |
| `cacat` | **target**: 1 = cacat, 0 = lolos QC |

Pengetahuan proses yang bisa dipakai buat bikin fitur:
- Tiap bahan punya suhu leleh dan suhu cetakan idealnya sendiri (PP sekitar 230/40 °C, ABS 240/60 °C,
  PC 300/90 °C). Yang bikin cacat adalah **seberapa jauh dari ideal**, bukan angka mentahnya.
- ABS dan PC menyerap air. Bahan yang lembap bikin cacat *silver streak*.

## Cara menilai

- **Metrik utama: PR-AUC.** Cacat cuma sekitar 8%, jadi akurasi menipu (sama kayak P2).
- Split stratified: train / validation / test.
- Tentukan threshold dengan alasan bisnis. Asumsi: part cacat yang lolos ke pelanggan merugikan
  **Rp 2.000.000** (klaim + reputasi), memisahkan part yang sebenarnya bagus merugikan **Rp 15.000**.

## Baseline wajib

**Logistic regression** dengan fitur asli (setelah dibersihkan). Laporkan PR-AUC-nya, lalu kalahkan.

## App untuk siapa

Operator mesin di lantai produksi. Input: bahan, mesin, dan parameter proses. Output: probabilitas cacat dan
saran tindakan (misalnya "cek suhu leleh, terlalu jauh dari ideal").

## Catatan

Datanya kotor, sama kayak data mesin CNC di P2. Temukan sendiri masalahnya. Satu petunjuk: cek apakah semua
angka suhu masuk akal untuk satuan °C.
