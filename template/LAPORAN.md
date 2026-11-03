# Template laporan (maksimal 6 halaman)

Pakai struktur ini. Boleh ditulis di Google Docs atau Word lalu dikumpulkan sebagai PDF. Jumlah halaman di
kurung cuma perkiraan.

## 1. Masalah (½ halaman)

- Siapa kliennya dan siapa user app-nya?
- Keputusan apa yang dibantu model? Apa akibatnya kalau model salah?
- Metrik utama dan baseline dari brief, dan kenapa metrik itu yang cocok.

## 2. Data (1 halaman)

- Ukuran data dan arti kolom-kolom penting.
- **Tabel masalah data** yang ditemukan: jenis masalah, berapa baris, cara membereskan, dan alasannya.
- 2–3 temuan EDA yang paling berpengaruh ke model (dengan grafik).

## 3. Metode (1½ halaman)

- Fitur yang dibuat dan alasannya.
- Cara split data (acak, berdasarkan waktu, atau per kelompok) dan kenapa.
- Baseline, lalu model-model yang dicoba.
- Cara memilih model dan threshold (pakai validation).

## 4. Hasil (1 halaman)

- Tabel: baseline vs model-model lain, metrik di validation, lalu model final di test.
- Satu grafik yang paling menjelaskan hasilnya (confusion matrix, prediksi vs aktual, profil segmen, dan
  semacamnya).
- Fitur apa yang paling berpengaruh? Masuk akal tidak?

## 5. Aplikasi (1 halaman)

- Arsitektur: data → model → API → app (gambar sederhana).
- Screenshot app, input dan output.
- Bagaimana app menangani input yang aneh.

## 6. Keterbatasan dan langkah berikutnya (½ halaman)

- Kapan model ini tidak bisa dipercaya?
- Kalau dipakai sungguhan, apa yang perlu dipantau (data drift, performa)?

## Lampiran (tidak dihitung halaman)

- Link repo, app, dan video.
- Pembagian kerja anggota tim.
- Kalau pakai AI assistant: untuk bagian apa saja.
