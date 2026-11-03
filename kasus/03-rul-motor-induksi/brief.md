# Kasus 03 · Remaining useful life motor induksi

**Klien:** manajer maintenance grup pabrik dengan tiga plant (Cikarang, Karawang, Purwakarta).

> *"Kami punya ratusan motor pompa dan konveyor. Ganti motor itu butuh pesan dulu, bisa 2–4 minggu. Saya mau
> tahu: motor ini kira-kira masih bisa jalan berapa hari lagi? Biar motor penggantinya dipesan sebelum yang
> lama mati."*

## Yang diminta

Model yang memprediksi **sisa umur motor dalam hari** (*remaining useful life*, RUL) dari data sensor hari ini.

## Data

`data/raw.csv`: 300 motor dipantau tiap hari sejak dipasang sampai rusak (*run-to-failure*).
Satu baris = satu motor pada satu hari.

| Kolom | Arti |
|---|---|
| `motor_id` | ID motor |
| `tipe_motor` | daya nominal: 5.5kW, 11kW, 22kW |
| `lokasi` | plant tempat motor dipasang |
| `hari_operasi` | sudah berapa hari motor jalan |
| `beban_pct` | beban kerja hari itu (% dari nominal) |
| `arus_A` | arus rata-rata (A) |
| `tegangan_V` | tegangan suplai (V) |
| `suhu_belitan_C` | suhu belitan stator (°C) |
| `getaran_rms_mm_s` | getaran RMS (mm/s) |
| `kecepatan_rpm` | kecepatan putar |
| `rul_hari` | **target**: sisa hari sampai motor rusak |

## Aturan penting: split per motor

**Split berdasarkan `motor_id`**: motor yang ada di test tidak boleh muncul di train. Jelaskan di laporan
kenapa aturan ini perlu.

## Cara menilai

- **Metrik utama: MAE (hari) pada baris dengan `rul_hari` ≤ 60.** Yang paling penting buat klien adalah
  motor yang sudah dekat rusak, karena itu yang menentukan kapan pesan motor baru.
- Laporkan juga MAE di semua baris.

## Baseline wajib

**Linear regression** dengan fitur sensor asli. Laporkan MAE-nya (dua-duanya), lalu kalahkan.

## App untuk siapa

Planner maintenance. Input: tipe motor dan pembacaan sensor hari ini. Output: perkiraan sisa umur dan status
(aman / pesan pengganti sekarang / segera ganti).

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa siapa pun. Memeriksa, memahami, dan
membereskannya adalah bagian dari tugas kalian.
