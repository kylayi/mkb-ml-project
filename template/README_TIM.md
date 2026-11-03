# [Nama project] · Tim [nama tim]

> Salin file ini jadi `README.md` di repo tim kalian, lalu isi semua bagian dalam kurung siku.

**Kasus:** [nomor dan nama kasus] · **App:** [link app] · **Video:** [link video]

| Anggota | NIM | Bagian yang dikerjakan |
|---|---|---|
| [nama] | [NIM] | [misalnya EDA dan pembersihan data] |
| [nama] | [NIM] | [misalnya model dan evaluasi] |
| [nama] | [NIM] | [misalnya API dan app] |

## Masalah dan user

[2–3 kalimat: siapa usernya, keputusan apa yang dibantu model ini.]

## Data dan pembersihan

| Masalah yang ditemukan | Berapa baris | Cara membereskan |
|---|---|---|
| [misalnya duplikat] | [angka] | [drop_duplicates] |

## Hasil

| Model | [metrik utama] validation | [metrik utama] test |
|---|---|---|
| Baseline: [nama baseline] | | |
| [model final] | | |

Threshold yang dipakai: [angka] karena [alasan bisnis].

## Cara menjalankan

```bash
pip install -r requirements.txt
uvicorn app.api.main:app --reload       # API
streamlit run app/ui/streamlit_app.py   # app
```

## Struktur repo

```
notebooks/      notebook EDA sampai simpan model
data/           data mentah (dan data bersih kalau perlu)
src/features.py fitur, dipakai saat training dan prediksi
artifacts/      model.joblib + metadata.json
app/            API (FastAPI) dan UI (Streamlit)
```

## Keterbatasan

[Kapan model ini tidak bisa dipercaya? Data apa yang belum ada?]

## Checklist sebelum dikumpulkan

- [ ] Repo publik, semua anggota punya commit
- [ ] Notebook bisa dijalankan ulang dari atas sampai bawah tanpa error
- [ ] Baseline wajib dilaporkan dan dibandingkan
- [ ] Test set dibuka sekali di akhir
- [ ] `artifacts/metadata.json` berisi versi model, fitur input, threshold, dan metrik
- [ ] App bisa dibuka orang lain lewat link, termasuk dari HP
- [ ] App tidak crash kalau inputnya aneh
- [ ] Laporan maksimal 6 halaman, video maksimal 5 menit
