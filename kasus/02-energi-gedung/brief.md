# Kasus 02 · Konsumsi energi gedung

**Klien:** building manager gedung kantor 8 lantai di Bandung.

> *"Tagihan listrik kami naik terus. Saya mau tahu besok kira-kira butuh listrik berapa per jam, biar bisa
> atur jadwal chiller dan negosiasi kontrak daya. Kalau konsumsi aslinya jauh di atas prediksi, berarti ada
> yang boros dan harus dicek."*

## Yang diminta

Model yang memprediksi **konsumsi listrik (kWh) per jam untuk besok**.

## Data

`data/raw.csv`: satu baris = satu jam, Januari 2024 – Juni 2026.

| Kolom | Arti |
|---|---|
| `waktu` | awal jam (waktu lokal) |
| `suhu_luar_C` | suhu udara luar dari sensor atap (°C) |
| `kelembaban_luar_pct` | kelembaban udara luar (%) |
| `okupansi_orang` | jumlah orang di gedung (dari turnstile) |
| `hari_libur` | 1 = libur nasional |
| `konsumsi_kWh` | **target**: konsumsi listrik jam itu |

## Aturan penting: jangan pakai data masa depan

Prediksi dibuat **hari ini untuk besok**. Jadi:
- Fitur jam, hari, libur, prakiraan suhu, dan jadwal okupansi boleh dipakai (semuanya bisa diketahui sehari
  sebelumnya).
- Konsumsi masa lalu boleh dipakai sebagai fitur **asal minimal 24 jam ke belakang** (lag ≥ 24 jam).
  Konsumsi satu jam sebelumnya tidak boleh, karena besok jam itu belum terjadi.

## Cara menilai

- **Metrik utama: MAE (kWh).**
- **Split berdasarkan waktu**, bukan acak. Contoh: train sampai Februari 2026, validation Maret–April 2026,
  test Mei–Juni 2026.

## Baseline wajib

**"Sama dengan minggu lalu"**: prediksi jam ini = konsumsi di jam yang sama 7 hari sebelumnya (lag 168 jam).

## App untuk siapa

Building manager. Input: tanggal besok, prakiraan suhu, dan perkiraan jumlah orang. Output: grafik prediksi
konsumsi 24 jam dan totalnya.

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa siapa pun. Memeriksa, memahami, dan
membereskannya adalah bagian dari tugas kalian.
