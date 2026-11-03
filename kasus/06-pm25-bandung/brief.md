# Kasus 06 · Prakiraan PM2.5 Bandung

**Klien:** tim kesehatan lingkungan sebuah dinas kota (fiktif) yang mengelola lima sensor kualitas udara.

> "Kami ingin memberi peringatan kepada warga sebelum udara memburuk, bukan sesudahnya. Misalnya, pukul 15.00
> kami sudah bisa mengumumkan bahwa pukul 18.00 nanti PM2.5 di Soekarno-Hatta akan tinggi, sehingga warga yang
> memiliki asma sebaiknya memakai masker."

## Yang diminta

Model yang memprediksi **PM2.5 tiga jam ke depan** di setiap stasiun, berdasarkan data sampai jam saat ini.

## Data

`data/raw.csv`: satu baris adalah satu stasiun pada satu jam, Juli 2024–Juni 2026.

| Kolom | Arti |
|---|---|
| `waktu` | awal jam (seharusnya dalam WIB) |
| `stasiun` | Dago, Soekarno-Hatta, Cibeureum, Antapani, Ujungberung |
| `pm25_ugm3` | konsentrasi PM2.5 (µg/m³) |
| `suhu_C` | suhu udara (°C) |
| `kelembaban_pct` | kelembapan udara (%) |
| `kecepatan_angin_ms` | kecepatan angin (m/detik) |
| `arah_angin_deg` | arah angin (derajat) |
| `curah_hujan_mm` | curah hujan pada jam tersebut (mm) |

**Target dibuat sendiri:** untuk setiap stasiun, target adalah nilai `pm25_ugm3` tiga jam sesudahnya.

## Aturan penting

- Fitur hanya boleh memakai informasi sampai jam saat ini. PM2.5 jam ini, satu jam yang lalu, atau kemarin pada
  jam yang sama boleh dipakai. PM2.5 satu jam ke depan tidak boleh dipakai.
- **Data dibagi berdasarkan waktu.** Contoh: *train* sampai Februari 2026, *validation* Maret–April 2026, *test*
  Mei–Juni 2026.

## Cara menilai

- **Metrik utama: MAE (µg/m³).**
- Laporkan juga seberapa sering model berhasil memperingatkan jam dengan PM2.5 di atas 55 µg/m³ (kategori
  "tidak sehat").

## *Baseline* wajib

**"Tiga jam lagi sama dengan sekarang"** (*persistence*): prediksi sama dengan nilai PM2.5 pada jam ini.

## Aplikasi untuk siapa

Warga dan petugas dinas. Masukan: stasiun dan kondisi saat ini. Keluaran: prakiraan PM2.5 tiga jam lagi,
kategorinya (baik, sedang, tidak sehat), dan saran.

## Istilah

| Istilah | Arti |
|---|---|
| PM2.5 | Partikel debu halus berdiameter 2,5 mikrometer atau lebih kecil. Cukup kecil untuk masuk ke paru-paru. |
| µg/m³ | Mikrogram per meter kubik: banyaknya partikel di setiap meter kubik udara. |
| WIB, UTC | Waktu Indonesia Barat dan waktu universal. WIB tujuh jam lebih cepat daripada UTC. |
| *Persistence* | *Baseline* deret waktu yang menganggap nilai di masa depan sama dengan nilai saat ini. |
| MAE, pembagian berdasarkan waktu | Lihat tabel istilah di README utama. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
