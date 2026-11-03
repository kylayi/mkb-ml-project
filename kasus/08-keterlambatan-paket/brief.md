# Kasus 08 · Prediksi Keterlambatan Paket

**Klien:** kepala operasional sebuah *hub* ekspedisi di Bandung (perusahaan fiktif).

> "Keluhan terbesar kami adalah paket terlambat, dan pelanggan paling kesal jika tidak diberi kabar. Jika dari
> data saat penjemputan kami sudah bisa tahu paket mana yang kemungkinan terlambat, kami dapat mengabari
> pelanggan lebih awal atau memprioritaskan paket tersebut."

## Yang diminta

Model yang menerima data satu paket saat dijemput dan menentukan apakah **paket tersebut akan terlambat**,
beserta probabilitasnya.

## Data

`data/raw.csv`: satu baris adalah satu paket dari *hub* Bandung, Januari 2025–Juni 2026.

| Kolom | Arti |
|---|---|
| `id_resi` | nomor resi |
| `tanggal_pickup` | tanggal paket dijemput |
| `jam_pickup` | jam paket dijemput (7–22) |
| `kota_tujuan` | kota tujuan |
| `jarak_km` | jarak dari Bandung (km) |
| `jumlah_transit` | jumlah *hub* transit yang dilalui |
| `layanan` | EXPRESS, REG, atau HEMAT |
| `janji_hari` | janji waktu tiba (SLA) dalam hari |
| `berat_kg` | berat paket (kg) |
| `metode_bayar` | COD atau non_COD |
| `cuaca_saat_pickup` | cerah, berawan, hujan, atau hujan_lebat |
| `volume_hub_hari` | jumlah paket yang masuk ke *hub* pada hari itu |
| `terlambat` | **target**: 1 = tiba melewati janji |

## Cara menilai

- **Metrik utama: PR-AUC.** Sekitar 18% paket terlambat.
- **Data dibagi berdasarkan waktu.** Contoh: *train* sampai Desember 2025, *validation* Januari–Maret 2026,
  *test* April–Juni 2026.
- Tentukan *threshold* berdasarkan alasan bisnis. Asumsinya: paket terlambat tanpa pemberitahuan memicu keluhan
  senilai **Rp50.000**, sedangkan pemberitahuan "kemungkinan terlambat" yang ternyata keliru merugikan
  **Rp5.000** (pelanggan bingung dan menghubungi layanan pelanggan).

## *Baseline* wajib

**Regresi logistik** dengan fitur asli. Laporkan PR-AUC-nya, lalu coba lampaui. Jika model yang lebih rumit
ternyata tidak lebih baik, hal itu juga merupakan temuan yang sah; jelaskan alasannya menurut kalian.

## Aplikasi untuk siapa

Staf layanan pelanggan dan operasional *hub*. Masukan: data paket saat dijemput. Keluaran: probabilitas
terlambat dan rekomendasi (kabari pelanggan, prioritaskan, atau aman).

## Istilah

| Istilah | Arti |
|---|---|
| *Hub* | Gudang pusat tempat paket dikumpulkan, disortir, lalu dikirim ke kota berikutnya. |
| Transit | Persinggahan paket di *hub* lain sebelum tiba di kota tujuan. |
| SLA | *Service level agreement*: janji waktu layanan, di sini janji jumlah hari sampai paket tiba. |
| COD | *Cash on delivery*: pembayaran dilakukan saat paket diterima. |
| Regresi logistik, PR-AUC, *threshold* | Lihat tabel istilah di README utama dan brief kasus 01. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
