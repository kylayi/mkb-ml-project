# Machine Learning · MKB UPI · Project kelompok (P4–P5)

Sekarang giliran kalian. Ulangi siklus **think → act → ship** dari P1–P3, kali ini dengan kasus baru dan tanpa
dipandu langkah demi langkah. P4 dan P5 tidak ada tatap muka: dua minggu itu dipakai buat mengerjakan project
ini bareng tim.

**Ringkasnya:** tim 3–4 orang dapat satu kasus secara acak, lalu menyerahkan repo, app yang bisa dibuka lewat
link, laporan, dan video demo.

Daftar isi: [kasus](#8-kasus) · [langkah kerja](#langkah-kerja) · [yang dikumpulkan](#yang-dikumpulkan-dan-penilaian) ·
[video](#video-demo-5-menit) · [timeline](#timeline) · [aturan](#aturan-main) · [pembagian kasus](#pembagian-kasus)

---

## 8 kasus

Semua datanya **sintetis** (data perusahaan asli hampir selalu rahasia) dan **sengaja kotor**, sama kayak data
mesin CNC di P2. Tiap kasus punya `brief.md`, perannya seperti permintaan plant manager di P2: siapa kliennya,
apa yang diminta, metriknya apa, dan baseline yang wajib dikalahkan.

| # | Kasus | Jenis tugas | Metrik utama | Data |
|---|---|---|---|---|
| 01 | [Quality control injection molding](kasus/01-qc-injection-molding/brief.md) | klasifikasi | PR-AUC | 6 ribu baris |
| 02 | [Konsumsi energi gedung](kasus/02-energi-gedung/brief.md) | regresi time series | MAE | 13 ribu jam |
| 03 | [Remaining useful life motor induksi](kasus/03-rul-motor-induksi/brief.md) | regresi | MAE | 120 motor, 33 ribu baris |
| 04 | [Diagnosis kerusakan bearing](kasus/04-diagnosis-bearing/brief.md) | klasifikasi multikelas | macro F1 | 4 ribu rekaman |
| 05 | [Segmentasi pelanggan UMKM](kasus/05-segmentasi-umkm/brief.md) | clustering · **challenge** | silhouette + profil | 3 ribu pelanggan |
| 06 | [Prakiraan PM2.5 Bandung](kasus/06-pm25-bandung/brief.md) | regresi time series | MAE | 3 stasiun × 1 tahun |
| 07 | [Irigasi pintar IoT](kasus/07-irigasi-pintar/brief.md) | klasifikasi | F1 | 8 petak × 3 bulan |
| 08 | [Keterlambatan paket](kasus/08-keterlambatan-paket/brief.md) | klasifikasi | PR-AUC | 12 ribu paket |

Kasus 05 tidak punya target (*unsupervised*) dan belum dibahas di kelas. Ambil kalau tim kalian siap belajar
mandiri.

---

## Langkah kerja

1. **Bikin repo publik tim.** Paling gampang: fork [mkb-ml-p3](https://github.com/nurhikam/mkb-ml-p3) (sudah
   ada FastAPI, Streamlit, Dockerfile, dan tes), ganti nama repo-nya, lalu salin folder kasus kalian dari repo
   ini. Semua anggota dijadikan collaborator.
2. **Think.** Baca `brief.md` bareng. Tulis di README: siapa usernya, keputusan apa yang dibantu model, metrik
   dan baseline-nya.
3. **Act.** Kerjakan di notebook seperti P2:
   - EDA dan bersih-bersih data, catat setiap masalah yang kalian temukan dan cara membereskannya
   - split sesuai aturan di brief (beberapa kasus wajib split berdasarkan waktu atau per motor)
   - baseline wajib dulu, baru model lain
   - pilih model dan threshold pakai **validation**, test dibuka sekali di akhir
   - simpan `model.joblib` + `metadata.json`, dan fitur di `src/features.py`
4. **Ship.** Ganti contoh model CNC di template P3 dengan model kalian: sesuaikan input API dan form Streamlit,
   lalu deploy ke Streamlit Community Cloud atau Hugging Face Spaces.
5. **Laporan dan video.** Template laporan ada di [`template/LAPORAN.md`](template/LAPORAN.md).

Checklist README repo tim ada di [`template/README_TIM.md`](template/README_TIM.md).

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
| P3 | tim dan kasus dibagi |
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

---

## Pembagian kasus

Kasus diacak di kelas pakai [`bagi_kasus.py`](bagi_kasus.py) dengan seed yang ditampilkan, jadi siapa pun bisa
menjalankan ulang dan dapat hasil yang sama:

```bash
python bagi_kasus.py --seed 2026 "Tim A" "Tim B" "Tim C"
```
