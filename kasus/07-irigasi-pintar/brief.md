# Kasus 07 · Irigasi pintar IoT

**Klien:** pengelola greenhouse sayur di Lembang dengan delapan petak dan sensor IoT di tiap petak.

> *"Agronom kami yang memutuskan kapan petak harus disiram, dan dia nggak bisa standby 24 jam. Saya mau sistem
> yang bisa ngasih notifikasi: petak ini perlu disiram sekarang. Tapi jangan nyiram kalau sebentar lagi mau
> hujan, sayang airnya."*

## Yang diminta

Model yang tiap jam menjawab untuk tiap petak: **perlu disiram sekarang atau tidak**.

## Data

`data/irigasi.csv`: satu baris = satu petak pada satu jam, Agustus–Oktober 2025.

| Kolom | Arti |
|---|---|
| `waktu` | awal jam |
| `petak` | P01 sampai P08 |
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

Pengetahuan yang bisa dipakai: tiap tanaman punya batas kelembaban tanah aman yang beda (selada paling haus,
cabai paling tahan kering). Tanah pasir cepat kering, tanah liat lambat. Agronom juga cuma menyiram siang hari.

## Cara menilai

- **Metrik utama: F1** untuk kelas `perlu_siram = 1`. Kelas positifnya cuma sekitar 4–5%.
- **Split berdasarkan waktu.** Contoh: train Agustus–September, validation 1–14 Oktober, test 15–31 Oktober.
- Bahas trade-off-nya: telat nyiram bikin tanaman stres, nyiram percuma buang air dan bikin akar busuk.

## Baseline wajib

**Aturan sederhana tanpa ML:** siram kalau `kelembaban_tanah_pct` < 35. Laporkan F1-nya, lalu tunjukkan
kenapa model kalian lebih baik (atau kenapa tidak).

## App untuk siapa

Pengelola greenhouse. Input: tanaman, jenis tanah, pembacaan sensor, dan prakiraan hujan. Output: perlu
disiram atau tidak, dan alasannya.

## Catatan

Datanya kotor. Petunjuk: sensor murah bisa macet (nilainya nggak berubah berjam-jam) atau ngasih angka yang
mustahil. Cek juga penulisan nama tanaman.
