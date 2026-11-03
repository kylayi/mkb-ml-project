# Kasus 08 · Prediksi keterlambatan paket

**Klien:** kepala operasional hub ekspedisi di Bandung (perusahaan fiktif).

> *"Komplain terbesar kami itu paket telat, dan pelanggan paling kesal kalau nggak dikabari. Kalau dari data
> waktu pickup kami sudah bisa tahu paket mana yang kemungkinan telat, kami bisa kabari pelanggan duluan atau
> prioritaskan paketnya."*

## Yang diminta

Model yang menerima data satu paket saat di-pickup dan menjawab: **paket ini bakal terlambat atau tidak**,
lengkap dengan probabilitasnya.

## Data

`data/raw.csv`: satu baris = satu paket dari hub Bandung, Januari 2025 – Juni 2026.

| Kolom | Arti |
|---|---|
| `id_resi` | nomor resi |
| `tanggal_pickup` | tanggal paket diambil |
| `jam_pickup` | jam paket diambil (7–22) |
| `kota_tujuan` | kota tujuan |
| `jarak_km` | jarak dari Bandung (km) |
| `jumlah_transit` | jumlah hub transit yang dilewati |
| `layanan` | EXPRESS, REG, HEMAT |
| `janji_hari` | janji waktu sampai (SLA) dalam hari |
| `berat_kg` | berat paket (kg) |
| `metode_bayar` | COD atau non_COD |
| `cuaca_saat_pickup` | cerah, berawan, hujan, hujan_lebat |
| `volume_hub_hari` | jumlah paket yang masuk hub hari itu |
| `terlambat` | **target**: 1 = sampai melewati janji |

## Cara menilai

- **Metrik utama: PR-AUC.** Sekitar 18% paket terlambat.
- **Split berdasarkan waktu.** Contoh: train sampai Desember 2025, validation Januari–Maret 2026, test
  April–Juni 2026.
- Tentukan threshold dengan alasan bisnis. Asumsi: paket telat tanpa pemberitahuan memicu komplain senilai
  **Rp 50.000**, notifikasi "mungkin telat" yang ternyata salah merugikan **Rp 5.000** (pelanggan bingung, CS
  ditelepon).

## Baseline wajib

**Logistic regression** dengan fitur asli. Laporkan PR-AUC-nya, lalu coba kalahkan. Kalau ternyata model yang
lebih rumit tidak lebih baik, itu juga temuan yang sah. Jelaskan kenapa menurut kalian.

## App untuk siapa

Staf CS dan operasional hub. Input: data paket saat pickup. Output: probabilitas terlambat dan rekomendasi
(kabari pelanggan / prioritaskan / aman).

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa siapa pun. Memeriksa, memahami, dan
membereskannya adalah bagian dari tugas kalian.
