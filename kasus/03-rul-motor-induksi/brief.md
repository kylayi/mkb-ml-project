# Kasus 03 · Sisa Umur Pakai Motor Induksi

**Klien:** manajer pemeliharaan sebuah grup pabrik dengan tiga lokasi (Cikarang, Karawang, dan Purwakarta).

> "Kami memiliki ratusan motor pompa dan konveyor. Mengganti motor harus memesan terlebih dahulu, dan
> pengirimannya bisa memakan waktu 2–4 minggu. Saya ingin tahu berapa hari lagi motor ini masih bisa bekerja,
> agar motor pengganti sudah dipesan sebelum motor lama rusak."

## Yang diminta

Model yang memprediksi **sisa umur pakai motor dalam hari** (*remaining useful life*, RUL) dari data sensor hari
ini.

## Data

`data/raw.csv`: 300 motor dipantau setiap hari sejak dipasang sampai rusak (*run-to-failure*). Satu baris adalah
satu motor pada satu hari.

| Kolom | Arti |
|---|---|
| `motor_id` | nomor identitas motor |
| `tipe_motor` | daya nominal: 5.5kW, 11kW, atau 22kW |
| `lokasi` | lokasi pabrik tempat motor dipasang |
| `hari_operasi` | jumlah hari motor sudah bekerja |
| `beban_pct` | beban kerja hari itu (% dari daya nominal) |
| `arus_A` | arus listrik rata-rata (ampere) |
| `tegangan_V` | tegangan listrik (volt) |
| `suhu_belitan_C` | suhu kumparan kawat di dalam motor (°C) |
| `getaran_rms_mm_s` | besar getaran (mm/detik) |
| `kecepatan_rpm` | kecepatan putar (putaran per menit) |
| `rul_hari` | **target**: sisa hari sampai motor rusak |

## Aturan penting: pembagian per motor

**Data dibagi berdasarkan `motor_id`:** motor yang ada di data *test* tidak boleh muncul di data *train*.
Jelaskan di laporan mengapa aturan ini diperlukan.

## Cara menilai

- **Metrik utama: MAE (hari) pada baris dengan `rul_hari` ≤ 60.** Bagi klien, yang paling penting adalah motor
  yang sudah mendekati rusak karena motor itulah yang menentukan kapan motor baru harus dipesan.
- Laporkan juga MAE pada semua baris.

## *Baseline* wajib

**Regresi linear** dengan fitur sensor asli. Laporkan kedua MAE-nya, lalu lampaui.

## Aplikasi untuk siapa

Perencana pemeliharaan. Masukan: tipe motor dan pembacaan sensor. Keluaran: perkiraan sisa umur dan status
(aman, pesan pengganti sekarang, atau segera ganti).

## Istilah

| Istilah | Arti |
|---|---|
| Motor induksi | Jenis motor listrik yang paling banyak dipakai di industri, misalnya untuk pompa, kipas, dan konveyor. |
| RUL | *Remaining useful life*: perkiraan sisa waktu sampai suatu mesin tidak bisa dipakai lagi. |
| *Run-to-failure* | Data yang mencatat mesin sejak baru sampai rusak, sehingga sisa umurnya pada setiap hari diketahui. |
| Belitan | Kumparan kawat tembaga di dalam motor. Suhu belitan yang tinggi mempercepat kerusakan isolasi. |
| RMS | *Root mean square*: cara menghitung "rata-rata kekuatan" sinyal getaran. |
| Regresi linear | Model regresi paling sederhana: target ditebak dari jumlah fitur yang masing-masing dikalikan bobot. |
| MAE | Lihat tabel istilah di README utama. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
