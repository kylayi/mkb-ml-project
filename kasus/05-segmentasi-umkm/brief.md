# Kasus 05 · Segmentasi pelanggan UMKM (challenge)

**Klien:** pemilik UMKM toko roti dan kopi di Bandung, punya aplikasi member sendiri.

> *"Saya punya 3.000 member, tapi promonya saya kirim ke semua orang sama rata. Boros. Saya mau tahu
> pelanggan saya itu ada tipe apa aja, biar promonya pas: yang setia dikasih apa, yang mulai jarang datang
> dikasih apa."*

## Kenapa ini challenge

Kasus lain punya **target** (jawaban yang benar). Kasus ini **tidak punya**. Tugasnya justru menemukan
kelompok pelanggan sendiri (*clustering*, *unsupervised learning*), yang belum dibahas di kelas. Pilih kasus
ini kalau tim kalian siap belajar mandiri.

## Yang diminta

1. Kelompokkan pelanggan jadi beberapa segmen yang **masuk akal secara bisnis**.
2. Beri nama dan profil tiap segmen (misalnya "pelanggan setia: datang 4–5 kali seminggu, jarang pakai
   promo").
3. Kasih **satu rekomendasi tindakan** per segmen.
4. Model yang bisa menempatkan **pelanggan baru** ke salah satu segmen.

## Data

`data/pelanggan_umkm.csv`: satu baris = satu member, data 6 bulan terakhir (sampai Juni 2026).

| Kolom | Arti |
|---|---|
| `id_pelanggan` | ID member |
| `tanggal_daftar` | tanggal jadi member |
| `umur` | umur (tahun) |
| `kecamatan` | domisili |
| `channel_utama` | paling sering beli lewat: toko, gofood, grabfood, shopeefood |
| `metode_bayar` | qris, tunai, ewallet, transfer |
| `kategori_favorit` | kopi, roti, kue_ulang_tahun, paket_snack |
| `jumlah_transaksi_6bln` | berapa kali belanja dalam 6 bulan |
| `total_belanja_rp` | total belanja 6 bulan (Rp) |
| `hari_sejak_transaksi_terakhir` | sudah berapa hari tidak belanja |
| `persen_pakai_promo` | persen transaksi yang pakai promo |
| `rating_rata` | rata-rata rating yang diberikan |

Fitur yang paling sering dipakai di segmentasi retail disebut **RFM**: *recency* (kapan terakhir belanja),
*frequency* (seberapa sering), dan *monetary* (berapa banyak uangnya).

## Cara menilai

Tidak ada jawaban benar tunggal, jadi yang dinilai:
- **Alasan memilih jumlah segmen**: pakai *elbow method* dan/atau *silhouette score*, lalu cek apakah
  hasilnya masuk akal dibaca manusia. Silhouette tertinggi belum tentu segmen terbaik buat bisnis.
- **Profil tiap segmen** dengan angka (rata-rata, median) dan visualisasi.
- **Rekomendasi** yang nyambung dengan profilnya.
- Fitur yang skalanya beda jauh (rupiah vs persen) harus diskalakan dulu. Jelaskan caranya.

## Baseline wajib

**K-Means** dengan fitur RFM yang sudah diskalakan. Laporkan silhouette score untuk beberapa nilai k, lalu
coba perbaiki (fitur lain, transformasi log, algoritma lain).

## App untuk siapa

Pemilik UMKM. Input: data satu pelanggan. Output: segmen pelanggan itu dan promo yang disarankan.

## Catatan

Datanya kotor. Petunjuk: cek tipe data `total_belanja_rp` setelah dibaca pandas, dan apakah satu
`id_pelanggan` bisa muncul lebih dari sekali.
