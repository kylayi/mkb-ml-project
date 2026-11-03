# Kasus 05 · Segmentasi Pelanggan UMKM (Tantangan)

**Klien:** pemilik UMKM toko roti dan kopi di Bandung yang memiliki aplikasi anggota (*member*) sendiri.

> "Saya punya 10.000 anggota, tetapi promo saya kirim ke semua orang dengan isi yang sama. Itu boros. Saya ingin
> tahu pelanggan saya terdiri atas tipe apa saja, agar promonya tepat sasaran: apa yang diberikan kepada
> pelanggan setia, dan apa yang diberikan kepada pelanggan yang mulai jarang datang."

## Mengapa kasus ini menjadi tantangan

Kasus lain memiliki **target** (jawaban yang benar). Kasus ini **tidak**. Tugasnya justru menemukan sendiri
kelompok-kelompok pelanggan (*clustering*, *unsupervised learning*), yang belum dibahas di kelas. Pilih kasus ini
jika tim kalian siap belajar secara mandiri.

## Yang diminta

1. Kelompokkan pelanggan menjadi beberapa segmen yang **masuk akal secara bisnis**.
2. Beri nama dan profil setiap segmen.
3. Berikan **satu rekomendasi tindakan** untuk setiap segmen.
4. Model yang dapat menempatkan **pelanggan baru** ke salah satu segmen.

## Data

`data/raw.csv`: satu baris adalah satu anggota, berisi data enam bulan terakhir (sampai Juni 2026).

| Kolom | Arti |
|---|---|
| `id_pelanggan` | nomor identitas anggota |
| `tanggal_daftar` | tanggal mendaftar sebagai anggota |
| `umur` | umur (tahun) |
| `kecamatan` | kecamatan tempat tinggal |
| `channel_utama` | saluran pembelian yang paling sering dipakai: toko, gofood, grabfood, shopeefood |
| `metode_bayar` | qris, tunai, ewallet, atau transfer |
| `kategori_favorit` | kopi, roti, kue_ulang_tahun, atau paket_snack |
| `jumlah_transaksi_6bln` | jumlah transaksi dalam enam bulan |
| `total_belanja_rp` | total belanja enam bulan (rupiah) |
| `hari_sejak_transaksi_terakhir` | jumlah hari sejak transaksi terakhir |
| `persen_pakai_promo` | persentase transaksi yang memakai promo |
| `rating_rata` | rata-rata penilaian yang diberikan (1–5) |

## Cara menilai

Tidak ada satu jawaban yang benar, sehingga yang dinilai adalah:
- **alasan memilih jumlah segmen**, dengan ukuran yang dapat dipertanggungjawabkan dan hasil yang masuk akal
  dibaca manusia;
- **profil setiap segmen** dengan angka (rata-rata atau median) dan visualisasi;
- **rekomendasi** yang sesuai dengan profilnya;
- langkah praproses dan alasannya.

## *Baseline* wajib

**K-Means.** Laporkan *silhouette score* untuk beberapa nilai k, lalu coba perbaiki.

## Aplikasi untuk siapa

Pemilik UMKM. Masukan: data satu pelanggan. Keluaran: segmen pelanggan tersebut dan promo yang disarankan.

## Istilah

| Istilah | Arti |
|---|---|
| Segmentasi | Membagi pelanggan ke dalam kelompok yang perilakunya mirip. |
| *Clustering* (pengelompokan) | Teknik *machine learning* untuk menemukan kelompok dalam data tanpa label jawaban. |
| *Unsupervised learning* | Pembelajaran tanpa target; model hanya melihat pola dalam data. |
| K-Means | Algoritma pengelompokan yang membagi data menjadi k kelompok berdasarkan kedekatan jarak. Nilai k ditentukan sendiri. |
| *Silhouette score* | Ukuran −1 sampai 1 tentang seberapa jelas batas antarkelompok. Semakin tinggi semakin jelas. |
| Praproses | Langkah menyiapkan data sebelum masuk ke model, misalnya mengubah skala atau mengisi nilai kosong. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
