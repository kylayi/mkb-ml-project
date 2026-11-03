# Machine Learning · MKB UPI · Project kelompok (P4–P5)

Sekarang giliran kalian. Ulangi siklus **think → act → ship** dari P1–P3, kali ini dengan kasus baru dan tanpa
dipandu langkah demi langkah. P4 dan P5 tidak ada tatap muka: dua minggu itu dipakai buat mengerjakan project
ini bareng tim.

**Ringkasnya:** tim 3–4 orang dapat satu kasus secara acak, lalu menyerahkan repo, app yang bisa dibuka lewat
link, laporan, dan video demo.

Daftar isi: [kasus](#8-kasus) · [langkah kerja](#langkah-kerja) · [yang dikumpulkan](#yang-dikumpulkan-dan-penilaian) ·
[video](#video-demo-5-menit) · [timeline](#timeline) · [aturan](#aturan-main)

---

## 8 kasus

Tiap kasus berisi dua hal: `brief.md` (permintaan klien, seperti plant manager di P2) dan `data/raw.csv`
(data mentah dari sistem klien). Datanya **sintetis**, karena data perusahaan asli hampir selalu rahasia,
dan **belum dibersihkan**. Tidak ada kode bantuan: memahami data, membersihkan, memilih fitur, dan memilih
model sepenuhnya keputusan tim kalian.

| # | Kasus | Jenis tugas | Metrik utama | Data |
|---|---|---|---|---|
| 01 | [Quality control injection molding](kasus/01-qc-injection-molding/brief.md) | klasifikasi | PR-AUC | 25 ribu siklus |
| 02 | [Konsumsi energi gedung](kasus/02-energi-gedung/brief.md) | regresi time series | MAE | 2,5 tahun per jam (22 ribu baris) |
| 03 | [Remaining useful life motor induksi](kasus/03-rul-motor-induksi/brief.md) | regresi | MAE | 300 motor (80 ribu baris) |
| 04 | [Diagnosis kerusakan bearing](kasus/04-diagnosis-bearing/brief.md) | klasifikasi multikelas | macro F1 | 15 ribu rekaman |
| 05 | [Segmentasi pelanggan UMKM](kasus/05-segmentasi-umkm/brief.md) | clustering · **challenge** | silhouette + profil | 10 ribu pelanggan |
| 06 | [Prakiraan PM2.5 Bandung](kasus/06-pm25-bandung/brief.md) | regresi time series | MAE | 5 stasiun × 2 tahun (88 ribu baris) |
| 07 | [Irigasi pintar IoT](kasus/07-irigasi-pintar/brief.md) | klasifikasi | F1 | 16 petak × 3 bulan (35 ribu baris) |
| 08 | [Keterlambatan paket](kasus/08-keterlambatan-paket/brief.md) | klasifikasi | PR-AUC | 40 ribu paket |

Kasus 05 tidak punya target (*unsupervised*) dan belum dibahas di kelas. Ambil kalau tim kalian siap belajar
mandiri.

---

## Langkah kerja

Ulangi **think → act → ship** seperti P1–P3. Caranya bebas, asal semua yang dikumpulkan lengkap dan aturan di
brief dipatuhi.

- **Repo:** satu repo publik per tim, semua anggota jadi collaborator. Boleh mulai dari fork
  [mkb-ml-p3](https://github.com/nurhikam/mkb-ml-p3) kalau mau pakai lagi struktur API dan Streamlit dari P3.
- **README repo:** checklist ada di [`template/README_TIM.md`](template/README_TIM.md).
- **Laporan:** kerangka ada di [`template/LAPORAN.md`](template/LAPORAN.md).

---

## Yang dikumpulkan dan penilaian

**Baseline wajib, algoritma bebas.**

| Bobot | Bagian | Isi |
|---|---|---|
| **40%** | Repository | notebook yang rapi dan bisa dijalankan ulang, `src/features.py`, artifact + metadata, README |
| **40%** | App / API | link yang bisa dibuka, menerima input, dan menampilkan prediksi |
| **20%** | Laporan + video | laporan maksimal 6 halaman, video maksimal 5 menit |

Laporan dinilai dosen pengampu. Praktisi mungkin ikut me-review repo dan app.

---

## Video demo (5 menit)

| Waktu | Isi |
|---|---|
| 30 detik | masalahnya apa dan siapa usernya |
| 90 detik | arsitektur dari ujung ke ujung: data → model → API → app |
| 90 detik | live demo, termasuk satu input yang aneh (kosong, mustahil, di luar rentang) |
| 60 detik | hasil, dibandingkan baseline, dan keterbatasan model |
| 30 detik | cadangan, biar tetap di bawah 5 menit |

**Setiap anggota menjelaskan bagiannya sendiri.**

---

## Timeline

| Kapan | Target |
|---|---|
| P3 | tim dibentuk, kasus diacak di kelas |
| Akhir minggu P4 | **checkpoint 1:** repo publik berisi EDA, data bersih, dan baseline |
| Pertengahan minggu P5 | **checkpoint 2:** app sudah online (boleh masih pakai model baseline) |
| Akhir minggu P5 | **deadline:** model final, laporan, dan video |

Tanggal pastinya dan link pengumpulan diumumkan dosen pengampu.

---

## Aturan main

- **AI assistant boleh** (ChatGPT, Gemini, Claude, Copilot), asal kalian paham setiap baris yang dikumpulkan.
  Siap-siap ditanya "baris ini ngapain?".
- **Web only dan tabular only.** Belum ada mobile app kali ini.
- **Test set dibuka sekali di akhir.** Jangan bohongi diri sendiri (ingat P2).
- **Mentok?** Tanya di QnA kelas dan tempel pesan error lengkapnya.
