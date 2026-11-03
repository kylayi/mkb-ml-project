# Kerangka Laporan (paling banyak 6 halaman)

Gunakan struktur berikut. Laporan boleh ditulis di Google Docs atau Word, lalu dikumpulkan dalam format PDF.
Jumlah halaman di dalam kurung hanya perkiraan.

## 1. Masalah (½ halaman)

- Siapa kliennya dan siapa pengguna aplikasinya?
- Keputusan apa yang dibantu oleh model? Apa akibatnya jika model keliru?
- Metrik utama dan *baseline* dari *brief*, serta alasan metrik tersebut sesuai.

## 2. Data (1 halaman)

- Ukuran data dan arti kolom-kolom yang penting.
- **Tabel masalah data** yang ditemukan: jenis masalah, jumlah baris, cara menanganinya, dan alasannya.
- Dua atau tiga temuan EDA yang paling berpengaruh terhadap model, disertai grafik.

## 3. Metode (1½ halaman)

- Fitur yang dibuat dan alasannya.
- Cara membagi data (acak, berdasarkan waktu, atau per kelompok) dan alasannya.
- *Baseline*, lalu model-model lain yang dicoba.
- Cara memilih model dan *threshold* (menggunakan data *validation*).

## 4. Hasil (1 halaman)

- Tabel perbandingan *baseline* dengan model lain pada data *validation*, lalu hasil model final pada data
  *test*.
- Satu grafik yang paling menjelaskan hasil (misalnya *confusion matrix*, prediksi dibandingkan nilai
  sebenarnya, atau profil segmen).
- Fitur apa yang paling berpengaruh? Apakah masuk akal?

## 5. Aplikasi (1 halaman)

- Arsitektur: data → model → API → aplikasi (gambar sederhana).
- Tangkapan layar aplikasi, beserta contoh masukan dan keluaran.
- Cara aplikasi menangani masukan yang tidak wajar.

## 6. Keterbatasan dan langkah berikutnya (½ halaman)

- Dalam kondisi apa model ini tidak dapat dipercaya?
- Jika dipakai sungguhan, apa yang perlu dipantau (misalnya perubahan pola data atau penurunan kinerja)?

## Lampiran (tidak dihitung dalam batas halaman)

- Tautan repositori, aplikasi, dan video.
- Pembagian kerja anggota tim.
- Jika menggunakan asisten AI: untuk bagian apa saja.
