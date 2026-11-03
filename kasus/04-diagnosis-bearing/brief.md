# Kasus 04 · Diagnosis kerusakan bearing

**Klien:** vibration analyst di pabrik semen.

> *"Kami rutin ngerekam getaran bearing motor dan pompa. Masalahnya, yang bisa baca spektrum getaran cuma saya
> sendiri, dan rekamannya ribuan. Saya mau sistem yang otomatis bilang: bearing ini normal, atau rusak di
> bagian mana. Biar teknisi tahu harus siapin part apa."*

## Yang diminta

Model yang menerima ringkasan satu rekaman getaran dan menjawab **kondisi bearing**: `normal`, `outer_race`
(cincin luar rusak), `inner_race` (cincin dalam rusak), atau `bola` (bola bearing rusak).

Ini **klasifikasi multikelas** (4 kelas), bukan ya/tidak.

## Data

`data/bearing.csv`: satu baris = satu rekaman getaran 1 detik yang sudah diringkas jadi angka.

| Kolom | Arti |
|---|---|
| `id_rekaman` | ID rekaman |
| `posisi_sensor` | `drive_end` (dekat beban) atau `fan_end` (jauh, sinyal lebih lemah) |
| `kecepatan_rpm` | kecepatan putar saat direkam |
| `beban_kN` | beban pada bearing (kN) |
| `suhu_housing_C` | suhu rumah bearing (°C) |
| `rms_g` | besar getaran rata-rata (g) |
| `puncak_g` | getaran tertinggi (g) |
| `kurtosis` | seberapa "runcing" sinyalnya; tumbukan dari kerusakan bikin kurtosis naik |
| `crest_factor` | puncak dibagi RMS |
| `energi_bpfo` | energi getaran di frekuensi khas kerusakan cincin luar |
| `energi_bpfi` | energi getaran di frekuensi khas kerusakan cincin dalam |
| `energi_bsf` | energi getaran di frekuensi khas kerusakan bola |
| `frekuensi_dominan_hz` | frekuensi dengan getaran terbesar |
| `kondisi` | **target** |

Pengetahuan yang bisa dipakai: frekuensi khas kerusakan sebanding dengan kecepatan putar. Membagi
`frekuensi_dominan_hz` dengan frekuensi putar (rpm / 60) bisa jadi fitur yang kuat.

## Cara menilai

- **Metrik utama: macro F1.** Kelasnya tidak seimbang (normal paling banyak), dan macro F1 memberi bobot sama
  ke tiap kelas, jadi kelas kecil (`bola`) ikut dinilai.
- Tampilkan **confusion matrix**: kerusakan apa yang paling sering tertukar?
- Split stratified: train / validation / test.

## Baseline wajib

**Logistic regression** (multikelas) dengan fitur asli. Laporkan macro F1-nya, lalu kalahkan.

## App untuk siapa

Teknisi maintenance. Input: hasil ringkasan rekaman getaran. Output: kondisi bearing, probabilitas tiap kelas,
dan part yang perlu disiapkan.

## Catatan

Datanya kotor. Petunjuk: label `kondisi` ditulis oleh beberapa teknisi berbeda. Hitung dulu ada berapa label
unik sebelum melatih model.
