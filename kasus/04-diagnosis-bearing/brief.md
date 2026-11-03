# Kasus 04 · Diagnosis Kerusakan *Bearing*

**Klien:** analis getaran di sebuah pabrik semen.

> "Kami rutin merekam getaran *bearing* pada motor dan pompa. Masalahnya, hanya saya yang bisa membaca
> spektrum getaran, sedangkan rekamannya ribuan. Saya ingin sistem yang otomatis mengatakan *bearing* ini normal
> atau rusak di bagian mana, agar teknisi tahu suku cadang apa yang perlu disiapkan."

## Yang diminta

Model yang menerima ringkasan satu rekaman getaran dan menentukan **kondisi *bearing***: `normal`, `outer_race`
(cincin luar rusak), `inner_race` (cincin dalam rusak), atau `bola` (bola *bearing* rusak).

Ini adalah **klasifikasi multikelas** (empat kelas), bukan sekadar ya/tidak.

## Data

`data/raw.csv`: satu baris adalah satu rekaman getaran berdurasi satu detik yang sudah diringkas menjadi
angka.

| Kolom | Arti |
|---|---|
| `id_rekaman` | nomor identitas rekaman |
| `posisi_sensor` | `drive_end` (sisi beban) atau `fan_end` (sisi kipas, lebih jauh dari beban) |
| `kecepatan_rpm` | kecepatan putar saat direkam (putaran per menit) |
| `beban_kN` | beban pada *bearing* (kilonewton) |
| `suhu_housing_C` | suhu rumah *bearing* (°C) |
| `rms_g` | besar getaran rata-rata (g) |
| `puncak_g` | getaran tertinggi (g) |
| `kurtosis` | ukuran seberapa "runcing" sinyal getaran |
| `crest_factor` | nilai puncak dibagi RMS |
| `energi_bpfo` | energi getaran pada frekuensi khas kerusakan cincin luar |
| `energi_bpfi` | energi getaran pada frekuensi khas kerusakan cincin dalam |
| `energi_bsf` | energi getaran pada frekuensi khas kerusakan bola |
| `frekuensi_dominan_hz` | frekuensi dengan getaran terbesar (hertz) |
| `kondisi` | **target** |

## Cara menilai

- **Metrik utama: *macro* F1.**
- Tampilkan ***confusion matrix***: jenis kerusakan apa yang paling sering tertukar?
- Data dibagi secara *stratified* menjadi *train*, *validation*, dan *test*.

## *Baseline* wajib

**Regresi logistik** (multikelas) dengan fitur asli. Laporkan *macro* F1-nya, lalu lampaui.

## Aplikasi untuk siapa

Teknisi pemeliharaan. Masukan: ringkasan rekaman getaran. Keluaran: kondisi *bearing*, probabilitas setiap
kelas, dan suku cadang yang perlu disiapkan.

## Istilah

| Istilah | Arti |
|---|---|
| *Bearing* (bantalan) | Komponen yang menopang poros berputar. Terdiri atas cincin luar, cincin dalam, dan bola-bola di antaranya. |
| *Outer race*, *inner race* | Cincin luar dan cincin dalam *bearing*, tempat bola menggelinding. |
| g | Satuan percepatan getaran; 1 g sama dengan percepatan gravitasi bumi. |
| Kurtosis | Ukuran statistik yang tinggi jika sinyal sering mengandung lonjakan tajam, misalnya akibat bola menghantam bagian yang retak. |
| *Crest factor* | Perbandingan nilai puncak dengan nilai RMS. Naik ketika ada hentakan sesaat. |
| BPFO, BPFI, BSF | Frekuensi khas yang muncul jika cincin luar, cincin dalam, atau bola rusak. Nilainya bergantung pada ukuran *bearing* dan kecepatan putar. |
| *Macro* F1 | Rata-rata skor F1 dari setiap kelas dengan bobot yang sama, sehingga kelas yang datanya sedikit tetap ikut dinilai. |
| *Confusion matrix* | Tabel yang membandingkan kelas sebenarnya dengan kelas hasil tebakan model. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
