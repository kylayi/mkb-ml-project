"""Nama, profil, dan promo setiap segmen + aturan memberi nama cluster K-Means.

Urutan kunci INFO_SEGMEN juga menjadi urutan warna tetap di semua grafik.
"""

INFO_SEGMEN = {
    "Pelanggan Setia": {
        "warna": "#2a78d6",
        "profil": "Sangat sering belanja (median ~28x/6 bln), baru saja datang, jarang memakai promo, "
                  "mayoritas beli langsung di toko.",
        "promo": "Program poin / member tier: hadiah non-diskon (gratis upgrade ukuran, akses menu baru "
                 "lebih dulu, free item di transaksi ke-10). Hindari diskon besar, mereka sudah membeli "
                 "dengan harga normal.",
    },
    "Pemburu Promo Online": {
        "warna": "#eb6834",
        "profil": "Belanja cukup rutin (~11x) dengan nilai kecil, hampir selalu memakai promo, "
                  "dominan lewat aplikasi ojek online.",
        "promo": "Promo bundling dengan minimum belanja (mis. beli 2 kopi + 1 roti hemat 15%) untuk "
                 "menaikkan nilai per transaksi, serta voucher khusus ambil di toko atau pesan via "
                 "aplikasi member agar tidak bergantung pada potongan ojol.",
    },
    "Pembeli Momen Spesial": {
        "warna": "#1baf7a",
        "profil": "Jarang belanja (~4x) tetapi nilai per transaksi sangat besar; favorit kue ulang tahun "
                  "& paket snack, usia lebih matang, hampir tidak butuh promo.",
        "promo": "Pengingat personal menjelang ulang tahun/acara + layanan pre-order kue, dan paket snack "
                 "box untuk kantor/arisan. Beri bonus (lilin, kartu ucapan, ongkir gratis), bukan diskon.",
    },
    "Mulai Menghilang": {
        "warna": "#eda100",
        "profil": "Sudah lama tidak datang (median ~110 hari), frekuensi dan belanja rendah, dan memberi "
                  "rating paling rendah (~3,6), sehingga ada indikasi pengalaman yang kurang memuaskan.",
        "promo": "Kampanye win-back: satu voucher kuat berbatas waktu (mis. diskon 30% berlaku 7 hari) "
                 "dengan pesan 'kami rindu kamu' + survei singkat 'apa yang bisa kami perbaiki?', "
                 "ditambah menu baru sebagai alasan untuk kembali.",
    },
}


def beri_nama_cluster(profil_median):
    """Petakan label cluster K-Means (angka acak) ke nama bisnis berdasarkan profil median.

    profil_median: DataFrame indeks=label cluster, kolom recency/frekuensi/basket/promo (skala asli).
    Aturan: recency tertinggi = Mulai Menghilang; basket tertinggi = Pembeli Momen Spesial;
    dari sisa, frekuensi tertinggi = Pelanggan Setia; terakhir = Pemburu Promo Online.
    """
    sisa = list(profil_median.index)
    peta = {}
    for kolom, nama in [("recency", "Mulai Menghilang"), ("basket", "Pembeli Momen Spesial"),
                        ("frekuensi", "Pelanggan Setia")]:
        label = profil_median.loc[sisa, kolom].idxmax()
        peta[label] = nama
        sisa.remove(label)
    peta[sisa[0]] = "Pemburu Promo Online"
    return {int(k): v for k, v in peta.items()}
