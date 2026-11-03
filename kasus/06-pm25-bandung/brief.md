# Kasus 06 · Prakiraan PM2.5 Bandung

**Klien:** tim kesehatan lingkungan dinas kota (fiktif) yang mengelola lima sensor kualitas udara.

> *"Kami mau kasih peringatan ke warga sebelum udaranya jelek, bukan setelahnya. Misalnya jam 3 sore sudah
> bisa bilang: jam 6 nanti PM2.5 di Soekarno-Hatta bakal tinggi, yang punya asma sebaiknya pakai masker."*

## Yang diminta

Model yang memprediksi **PM2.5 tiga jam ke depan** di tiap stasiun, dari data sampai jam sekarang.

## Data

`data/raw.csv`: satu baris = satu stasiun pada satu jam, Juli 2024 – Juni 2026.

| Kolom | Arti |
|---|---|
| `waktu` | awal jam (seharusnya waktu lokal WIB) |
| `stasiun` | Dago, Soekarno-Hatta, Cibeureum, Antapani, Ujungberung |
| `pm25_ugm3` | konsentrasi PM2.5 (µg/m³) |
| `suhu_C` | suhu udara (°C) |
| `kelembaban_pct` | kelembaban udara (%) |
| `kecepatan_angin_ms` | kecepatan angin (m/s) |
| `arah_angin_deg` | arah angin (derajat) |
| `curah_hujan_mm` | hujan jam itu (mm) |

**Target dibuat sendiri:** untuk tiap stasiun, target = `pm25_ugm3` tiga jam setelahnya.

## Aturan penting

- Fitur cuma boleh pakai informasi sampai jam sekarang. PM2.5 jam sekarang, 1 jam lalu, kemarin di jam yang
  sama: boleh. PM2.5 1 jam ke depan: tidak boleh.
- **Split berdasarkan waktu.** Contoh: train sampai Februari 2026, validation Maret–April, test Mei–Juni 2026.

## Cara menilai

- **Metrik utama: MAE (µg/m³).**
- Laporkan juga: seberapa sering model berhasil memperingatkan jam dengan PM2.5 di atas 55 µg/m³
  (kategori "tidak sehat").

## Baseline wajib

**"Tiga jam lagi sama dengan sekarang"** (*persistence*): prediksi = PM2.5 jam ini.

## App untuk siapa

Warga dan petugas dinas. Input: stasiun dan kondisi saat ini. Output: prakiraan PM2.5 tiga jam lagi dan
kategorinya (baik / sedang / tidak sehat), plus saran.

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa siapa pun. Memeriksa, memahami, dan
membereskannya adalah bagian dari tugas kalian.
