# Kasus 07 · Irigasi pintar IoT

**Klien:** pengelola greenhouse sayur di Lembang dengan enam belas petak dan sensor IoT di tiap petak.

> *"Agronom kami yang memutuskan kapan petak harus disiram, dan dia nggak bisa standby 24 jam. Saya mau sistem
> yang bisa ngasih notifikasi: petak ini perlu disiram sekarang. Tapi jangan nyiram kalau sebentar lagi mau
> hujan, sayang airnya."*

## Yang diminta

Model yang tiap jam menjawab untuk tiap petak: **perlu disiram sekarang atau tidak**.

## Data

`data/raw.csv`: satu baris = satu petak pada satu jam, Agustus–Oktober 2025.

| Kolom | Arti |
|---|---|
| `waktu` | awal jam |
| `petak` | P01 sampai P16 |
| `tanaman` | cabai, tomat, selada |
| `jenis_tanah` | pasir, lempung, liat |
| `umur_tanaman_hari` | umur tanaman sejak tanam (hari) |
| `kelembaban_tanah_pct` | kelembaban tanah dari sensor (%) |
| `suhu_udara_C` | suhu udara (°C) |
| `kelembaban_udara_pct` | kelembaban udara (%) |
| `cahaya_lux` | intensitas cahaya (lux) |
| `curah_hujan_mm` | hujan jam itu (mm) |
| `prakiraan_hujan_6jam_mm` | prakiraan total hujan 6 jam ke depan (mm) |
| `perlu_siram` | **target**: keputusan agronom, 1 = perlu disiram |

## Cara menilai

- **Metrik utama: F1** untuk kelas `perlu_siram = 1`.
- **Split berdasarkan waktu.** Contoh: train Agustus–September, validation 1–14 Oktober, test 15–31 Oktober.
- Bahas trade-off-nya: telat nyiram bikin tanaman stres, nyiram percuma buang air dan bikin akar busuk.

## Baseline wajib

**Aturan sederhana tanpa ML:** siram kalau `kelembaban_tanah_pct` < 35. Laporkan F1-nya, lalu tunjukkan
kenapa model kalian lebih baik (atau kenapa tidak).

## App untuk siapa

Pengelola greenhouse. Input: tanaman, jenis tanah, pembacaan sensor, dan prakiraan hujan. Output: perlu
disiram atau tidak, dan alasannya.

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa siapa pun. Memeriksa, memahami, dan
membereskannya adalah bagian dari tugas kalian.
