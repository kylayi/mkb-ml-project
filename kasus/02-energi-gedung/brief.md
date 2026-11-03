# Kasus 02 · Konsumsi Energi Gedung

**Klien:** pengelola gedung (*building manager*) sebuah gedung perkantoran delapan lantai di Bandung.

> "Tagihan listrik kami terus naik. Saya ingin tahu kebutuhan listrik besok per jam agar jadwal *chiller*
> bisa diatur dan kontrak daya bisa dinegosiasikan. Jika konsumsi sebenarnya jauh di atas prediksi, berarti ada
> pemborosan yang harus diperiksa."

## Yang diminta

Model yang memprediksi **konsumsi listrik (kWh) per jam untuk hari berikutnya**.

## Data

`data/raw.csv`: satu baris adalah satu jam, Januari 2024–Juni 2026.

| Kolom | Arti |
|---|---|
| `waktu` | awal jam (waktu setempat) |
| `suhu_luar_C` | suhu udara luar dari sensor di atap (°C) |
| `kelembaban_luar_pct` | kelembapan udara luar (%) |
| `okupansi_orang` | jumlah orang di dalam gedung (dari gerbang putar) |
| `hari_libur` | 1 = hari libur nasional |
| `konsumsi_kWh` | **target**: konsumsi listrik pada jam tersebut (kWh) |

## Aturan penting: jangan memakai data masa depan

Prediksi dibuat **hari ini untuk besok**. Oleh karena itu:
- Fitur jam, hari, hari libur, prakiraan suhu, dan jadwal okupansi boleh dipakai karena semuanya dapat
  diketahui sehari sebelumnya.
- Konsumsi masa lalu boleh dipakai sebagai fitur **asalkan paling sedikit 24 jam sebelumnya** (*lag* ≥ 24 jam).
  Konsumsi satu jam sebelumnya tidak boleh dipakai karena pada saat prediksi dibuat, jam tersebut belum terjadi.

## Cara menilai

- **Metrik utama: MAE (kWh).**
- **Data dibagi berdasarkan waktu**, bukan secara acak. Contoh: *train* sampai Februari 2026, *validation*
  Maret–April 2026, *test* Mei–Juni 2026.

## *Baseline* wajib

**"Sama dengan minggu lalu":** prediksi untuk suatu jam sama dengan konsumsi pada jam yang sama tujuh hari
sebelumnya (*lag* 168 jam).

## Aplikasi untuk siapa

Pengelola gedung. Masukan: tanggal besok, prakiraan suhu, dan perkiraan jumlah orang. Keluaran: grafik prediksi
konsumsi 24 jam beserta totalnya.

## Istilah

| Istilah | Arti |
|---|---|
| kWh | Kilowatt-jam, satuan energi listrik yang tertera di tagihan PLN. |
| *Chiller* | Mesin pendingin pusat untuk AC gedung, biasanya pemakai listrik terbesar. |
| Okupansi | Tingkat keterisian gedung, di sini dalam jumlah orang. |
| *Lag* | Nilai suatu kolom pada waktu sebelumnya. *Lag* 24 berarti nilai 24 jam yang lalu. |
| MAE, pembagian berdasarkan waktu | Lihat tabel istilah di README utama. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
