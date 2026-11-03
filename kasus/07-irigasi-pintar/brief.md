# Kasus 07 · Irigasi Pintar Berbasis IoT

**Klien:** pengelola rumah kaca (*greenhouse*) sayuran di Lembang dengan enam belas petak dan sensor IoT di
setiap petak.

> "Agronom kami yang memutuskan kapan suatu petak harus disiram, dan ia tidak bisa berjaga 24 jam. Saya ingin
> sistem yang memberi notifikasi bahwa suatu petak perlu disiram sekarang. Namun, jangan menyiram jika sebentar
> lagi akan hujan, karena itu membuang air."

## Yang diminta

Model yang setiap jam menentukan untuk setiap petak: **perlu disiram sekarang atau tidak**.

## Data

`data/raw.csv`: satu baris adalah satu petak pada satu jam, Agustus–Oktober 2025.

| Kolom | Arti |
|---|---|
| `waktu` | awal jam |
| `petak` | P01 sampai P16 |
| `tanaman` | cabai, tomat, atau selada |
| `jenis_tanah` | pasir, lempung, atau liat |
| `umur_tanaman_hari` | umur tanaman sejak ditanam (hari) |
| `kelembaban_tanah_pct` | kelembapan tanah menurut sensor (%) |
| `suhu_udara_C` | suhu udara (°C) |
| `kelembaban_udara_pct` | kelembapan udara (%) |
| `cahaya_lux` | intensitas cahaya (lux) |
| `curah_hujan_mm` | curah hujan pada jam tersebut (mm) |
| `prakiraan_hujan_6jam_mm` | prakiraan total hujan enam jam ke depan (mm) |
| `perlu_siram` | **target**: keputusan agronom, 1 = perlu disiram |

## Cara menilai

- **Metrik utama: F1** untuk kelas `perlu_siram = 1`.
- **Data dibagi berdasarkan waktu.** Contoh: *train* Agustus–September, *validation* 1–14 Oktober, *test*
  15–31 Oktober.
- Bahas pertimbangan biayanya: terlambat menyiram membuat tanaman stres, sedangkan menyiram tanpa perlu membuang
  air dan dapat membuat akar membusuk.

## *Baseline* wajib

**Aturan sederhana tanpa *machine learning*:** siram jika `kelembaban_tanah_pct` kurang dari 35. Laporkan
F1-nya, lalu tunjukkan mengapa model kalian lebih baik (atau mengapa tidak).

## Aplikasi untuk siapa

Pengelola rumah kaca. Masukan: tanaman, jenis tanah, pembacaan sensor, dan prakiraan hujan. Keluaran: perlu
disiram atau tidak, beserta alasannya.

## Istilah

| Istilah | Arti |
|---|---|
| IoT | *Internet of Things*: perangkat sensor yang mengirim data secara otomatis melalui internet. |
| Agronom | Ahli pertanian yang menentukan perawatan tanaman. |
| Lux | Satuan intensitas cahaya. Sinar matahari terik dapat mencapai sekitar 100.000 lux. |
| Lempung, liat, pasir | Jenis tanah. Pasir cepat kering, liat menahan air paling lama, lempung berada di antaranya. |
| F1, pembagian berdasarkan waktu | Lihat tabel istilah di README utama. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
