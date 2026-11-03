# Machine Learning · MKB UPI · Proyek Kelompok (P4–P5)

Sekarang giliran kalian. Ulangi siklus **think → act → ship** dari P1–P3, kali ini dengan kasus baru dan tanpa
dipandu langkah demi langkah. Pertemuan P4 dan P5 tidak diadakan secara tatap muka; dua minggu tersebut
digunakan untuk mengerjakan proyek ini bersama tim.

**Ringkasan:** setiap tim yang terdiri atas 3–4 orang mendapat satu kasus secara acak, lalu menyerahkan
repositori, aplikasi yang dapat dibuka melalui tautan, laporan, dan video demo.

Daftar isi: [kasus](#delapan-kasus) · [cara kerja](#cara-kerja) · [yang dikumpulkan](#yang-dikumpulkan-dan-penilaian) ·
[video](#video-demo-5-menit) · [jadwal](#jadwal) · [aturan](#aturan) · [istilah](#istilah-yang-sering-muncul)

---

## Delapan kasus

Setiap kasus berisi dua berkas: `brief.md` (permintaan klien, seperti permintaan *plant manager* di P2) dan
`data/raw.csv` (data mentah dari sistem klien). Datanya **sintetis** karena data perusahaan asli hampir selalu
bersifat rahasia, dan **belum dibersihkan**. Tidak ada kode bantuan: memahami data, membersihkannya, memilih
fitur, dan memilih model sepenuhnya menjadi keputusan tim kalian.

| No. | Kasus | Jenis tugas | Metrik utama | Ukuran data |
|---|---|---|---|---|
| 01 | [Pengendalian mutu *injection molding*](kasus/01-qc-injection-molding/brief.md) | klasifikasi | PR-AUC | 25 ribu siklus cetak |
| 02 | [Konsumsi energi gedung](kasus/02-energi-gedung/brief.md) | regresi deret waktu | MAE | 2,5 tahun per jam (22 ribu baris) |
| 03 | [Sisa umur pakai motor induksi](kasus/03-rul-motor-induksi/brief.md) | regresi | MAE | 300 motor (80 ribu baris) |
| 04 | [Diagnosis kerusakan *bearing*](kasus/04-diagnosis-bearing/brief.md) | klasifikasi multikelas | *macro* F1 | 15 ribu rekaman |
| 05 | [Segmentasi pelanggan UMKM](kasus/05-segmentasi-umkm/brief.md) | pengelompokan · **tantangan** | *silhouette* + profil | 10 ribu pelanggan |
| 06 | [Prakiraan PM2.5 Bandung](kasus/06-pm25-bandung/brief.md) | regresi deret waktu | MAE | 5 stasiun × 2 tahun (88 ribu baris) |
| 07 | [Irigasi pintar berbasis IoT](kasus/07-irigasi-pintar/brief.md) | klasifikasi | F1 | 16 petak × 3 bulan (35 ribu baris) |
| 08 | [Keterlambatan paket](kasus/08-keterlambatan-paket/brief.md) | klasifikasi | PR-AUC | 40 ribu paket |

Kasus 05 tidak memiliki target (*unsupervised learning*) dan belum dibahas di kelas. Pilih kasus ini hanya jika
tim kalian siap belajar secara mandiri.

---

## Cara kerja

Ulangi **think → act → ship** seperti di P1–P3. Caranya bebas, asalkan semua yang dikumpulkan lengkap dan
aturan di *brief* dipatuhi.

- **Repositori:** satu repositori publik untuk setiap tim, dan semua anggota dijadikan *collaborator*. Kalian
  boleh memulai dari *fork* [mkb-ml-p3](https://github.com/nurhikam/mkb-ml-p3) jika ingin memakai kembali
  struktur API dan Streamlit dari P3.
- **README repositori:** daftar periksanya ada di [`template/README_TIM.md`](template/README_TIM.md).
- **Laporan:** kerangkanya ada di [`template/LAPORAN.md`](template/LAPORAN.md).

---

## Yang dikumpulkan dan penilaian

**Model pembanding (*baseline*) wajib ada; algoritmanya bebas.**

| Bobot | Bagian | Isi |
|---|---|---|
| **40%** | Repositori | *notebook* yang rapi dan dapat dijalankan ulang, `src/features.py`, model + metadata, README |
| **40%** | Aplikasi / API | tautan yang dapat dibuka, menerima masukan, dan menampilkan prediksi |
| **20%** | Laporan + video | laporan paling banyak 6 halaman, video paling lama 5 menit |

Laporan dinilai oleh dosen pengampu. Praktisi dapat ikut meninjau repositori dan aplikasi.

---

## Video demo (5 menit)

| Durasi | Isi |
|---|---|
| 30 detik | masalah yang diselesaikan dan siapa penggunanya |
| 90 detik | arsitektur dari awal sampai akhir: data → model → API → aplikasi |
| 90 detik | demo langsung, termasuk satu masukan yang tidak wajar (kosong, mustahil, atau di luar rentang) |
| 60 detik | hasil, perbandingan dengan *baseline*, dan keterbatasan model |
| 30 detik | cadangan, agar video tetap di bawah 5 menit |

**Setiap anggota menjelaskan bagian yang dikerjakannya sendiri.**

---

## Jadwal

| Waktu | Target |
|---|---|
| P3 | tim dibentuk, kasus diundi di kelas |
| Akhir minggu P4 | **titik periksa 1:** repositori publik berisi EDA, data bersih, dan *baseline* |
| Pertengahan minggu P5 | **titik periksa 2:** aplikasi sudah daring (boleh masih memakai model *baseline*) |
| Akhir minggu P5 | **tenggat:** model final, laporan, dan video |

Tanggal pasti dan tautan pengumpulan akan diumumkan oleh dosen pengampu.

---

## Aturan

- **Asisten AI boleh digunakan** (ChatGPT, Gemini, Claude, Copilot), asalkan kalian memahami setiap baris yang
  dikumpulkan. Bersiaplah ditanya, "Baris ini berfungsi untuk apa?"
- **Hanya aplikasi web dan data tabel.** Aplikasi seluler belum termasuk kali ini.
- **Data uji (*test set*) dibuka satu kali, di akhir.** Jangan membohongi diri sendiri (ingat P2).
- **Menemui kendala?** Tanyakan di QnA kelas dan sertakan pesan galat (*error*) secara lengkap.

---

## Istilah yang sering muncul

| Istilah | Arti singkat |
|---|---|
| *Baseline* | Model atau aturan paling sederhana yang menjadi pembanding. Model kalian dianggap berguna jika lebih baik daripada *baseline*. |
| Fitur | Kolom masukan yang dipakai model untuk menebak. Fitur bisa diambil langsung dari data atau dibuat sendiri (misalnya selisih dua kolom). |
| Target | Kolom yang ingin ditebak, misalnya `cacat` atau `konsumsi_kWh`. |
| *Train*, *validation*, *test* | Tiga bagian data: untuk melatih model, untuk memilih model dan *threshold*, dan untuk ujian akhir yang dibuka sekali. |
| *Stratified split* | Pembagian data acak yang menjaga proporsi kelas tetap sama di setiap bagian. |
| Pembagian berdasarkan waktu | Data lama untuk melatih, data terbaru untuk menguji. Wajib untuk data deret waktu agar model tidak "melihat masa depan". |
| Klasifikasi | Menebak kategori, misalnya cacat/tidak cacat. |
| Regresi | Menebak angka, misalnya konsumsi listrik dalam kWh. |
| Deret waktu (*time series*) | Data yang dicatat berurutan menurut waktu, misalnya per jam. |
| *Threshold* | Batas probabilitas untuk memutuskan "ya". Probabilitas di atas batas dianggap "ya", di bawahnya "tidak". |
| PR-AUC | Ukuran 0–1 untuk klasifikasi dengan kelas langka: seberapa baik model menemukan kasus positif tanpa terlalu banyak alarm palsu. Semakin dekat ke 1 semakin baik. |
| F1 | Ukuran 0–1 yang menyeimbangkan *precision* (seberapa sering tebakan "ya" itu benar) dan *recall* (seberapa banyak kasus "ya" yang tertangkap). |
| MAE | *Mean absolute error*: rata-rata selisih antara tebakan dan nilai sebenarnya, dalam satuan target. Semakin kecil semakin baik. |
| *Artifact* | Hasil pelatihan yang disimpan: `model.joblib` (model) dan `metadata.json` (catatan versi, fitur, *threshold*, dan metrik). |
| EDA | *Exploratory data analysis*: mengenali data sebelum membuat model, misalnya dengan statistik ringkas dan grafik. |
