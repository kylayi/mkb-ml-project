# Kasus 01 · Quality control injection molding

**Klien:** kepala QC pabrik komponen plastik (tutup botol, housing, klip) di Cikarang.

> *"Part cacat baru ketahuan waktu inspeksi visual di akhir shift. Kalau mesin bisa ngasih tahu dari
> parameter prosesnya bahwa part ini kemungkinan cacat, part itu bisa langsung dipisahin dan settingan
> mesinnya dibetulkan sebelum ratusan part lain ikut cacat."*

## Yang diminta

Model yang menerima parameter satu siklus cetak dan menjawab: **part ini cacat atau tidak**, lengkap dengan
probabilitasnya.

## Data

`data/raw.csv`: satu baris = satu siklus cetak (satu part), 4 mesin, Maret–Juni 2026.

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

Info dari tim proses: suhu leleh dan suhu cetakan standar untuk PP sekitar 230/40 °C, ABS 240/60 °C, dan
PC 300/90 °C. ABS dan PC termasuk bahan yang menyerap air.

## Cara menilai

- **Metrik utama: PR-AUC.** Cacat sekitar 8%.
- Split stratified: train / validation / test.
- Tentukan threshold dengan alasan bisnis. Asumsi: part cacat yang lolos ke pelanggan merugikan
  **Rp 2.000.000** (klaim + reputasi), memisahkan part yang sebenarnya bagus merugikan **Rp 15.000**.

## Baseline wajib

**Logistic regression** dengan fitur asli (setelah dibersihkan). Laporkan PR-AUC-nya, lalu kalahkan.

## App untuk siapa

Operator mesin di lantai produksi. Input: bahan, mesin, dan parameter proses. Output: probabilitas cacat dan
saran tindakan (misalnya "cek suhu leleh, terlalu jauh dari ideal").

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa siapa pun. Memeriksa, memahami, dan
membereskannya adalah bagian dari tugas kalian.
