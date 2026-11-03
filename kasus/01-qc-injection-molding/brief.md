# Kasus 01 · Pengendalian Mutu *Injection Molding*

**Klien:** kepala bagian pengendalian mutu (*quality control*, QC) di pabrik komponen plastik (tutup botol,
rumah komponen, klip) di Cikarang.

> "Komponen cacat baru ketahuan saat inspeksi visual di akhir *shift*. Jika dari parameter proses mesin kami
> sudah bisa tahu bahwa suatu komponen kemungkinan cacat, komponen itu bisa langsung dipisahkan dan pengaturan
> mesin bisa diperbaiki sebelum ratusan komponen lain ikut cacat."

## Yang diminta

Model yang menerima parameter satu siklus cetak dan menjawab apakah **komponen tersebut cacat atau tidak**,
beserta probabilitasnya.

## Data

`data/raw.csv`: satu baris adalah satu siklus cetak (satu komponen) dari 4 mesin, Maret–Juni 2026.

| Kolom | Arti |
|---|---|
| `waktu_produksi` | waktu siklus cetak |
| `mesin` | IM-01 sampai IM-04 |
| `shift` | pagi, siang, malam |
| `bahan` | jenis plastik: PP, ABS, atau PC |
| `suhu_leleh_C` | suhu plastik cair di dalam *barrel* (°C) |
| `suhu_cetakan_C` | suhu cetakan (°C) |
| `tekanan_injeksi_bar` | tekanan saat plastik disuntikkan ke cetakan (bar) |
| `kecepatan_injeksi_mm_s` | kecepatan dorong *screw* (mm/detik) |
| `waktu_pendinginan_s` | lama komponen didinginkan di dalam cetakan (detik) |
| `waktu_siklus_s` | lama satu siklus penuh (detik) |
| `kelembaban_bahan_pct` | kadar air bahan sebelum dicetak (%) |
| `cacat` | **target**: 1 = cacat, 0 = lolos QC |

Informasi dari tim proses: suhu leleh dan suhu cetakan standar untuk PP sekitar 230/40 °C, ABS 240/60 °C, dan
PC 300/90 °C. ABS dan PC termasuk bahan yang menyerap air.

## Cara menilai

- **Metrik utama: PR-AUC.** Komponen cacat sekitar 8%.
- Data dibagi secara *stratified* menjadi *train*, *validation*, dan *test*.
- Tentukan *threshold* berdasarkan alasan bisnis. Asumsinya: komponen cacat yang lolos ke pelanggan merugikan
  **Rp500.000** (klaim dan reputasi), sedangkan komponen bagus yang ikut disisihkan merugikan **Rp25.000**.

## *Baseline* wajib

**Regresi logistik** dengan fitur asli (setelah data dibersihkan). Laporkan PR-AUC-nya, lalu lampaui.

## Aplikasi untuk siapa

Operator mesin di lantai produksi. Masukan: bahan, mesin, dan parameter proses. Keluaran: probabilitas cacat
dan saran tindakan.

## Istilah

| Istilah | Arti |
|---|---|
| *Injection molding* | Proses mencetak plastik: plastik dilelehkan, disuntikkan ke cetakan, didinginkan, lalu dikeluarkan. |
| *Barrel* dan *screw* | Tabung pemanas tempat plastik dilelehkan, dan ulir di dalamnya yang mendorong plastik ke cetakan. |
| PP, ABS, PC | Polipropilena, akrilonitril butadiena stirena, dan polikarbonat: tiga jenis plastik yang umum dipakai. |
| Menyerap air (higroskopis) | Bahan yang menyerap uap air dari udara. Jika dicetak dalam keadaan lembap, permukaan komponen dapat bergaris keperakan (*silver streak*). |
| Regresi logistik | Model klasifikasi sederhana yang menghasilkan probabilitas dari kombinasi linear fitur. |
| PR-AUC, *threshold*, *stratified* | Lihat tabel istilah di README utama. |

## Catatan

Data diekspor apa adanya dari sistem klien dan belum diperiksa oleh siapa pun. Memeriksa, memahami, dan
membersihkannya merupakan bagian dari tugas kalian.
