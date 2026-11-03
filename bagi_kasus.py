"""Acak kasus project ke tiap tim, adil dan bisa diulang.

    python bagi_kasus.py --seed 2026 "Tim A" "Tim B" "Tim C"
    python bagi_kasus.py --seed 2026 --jumlah 10          # tim diberi nama Tim 1..10

Kalau tim lebih banyak dari 8, kasus dipakai ulang secara merata (tidak ada kasus yang dipakai dua kali
sebelum semua kasus kebagian).
"""
import argparse
import random

KASUS = [
    "01 Quality control injection molding",
    "02 Konsumsi energi gedung",
    "03 Remaining useful life motor induksi",
    "04 Diagnosis kerusakan bearing",
    "05 Segmentasi pelanggan UMKM (challenge)",
    "06 Prakiraan PM2.5 Bandung",
    "07 Irigasi pintar IoT",
    "08 Keterlambatan paket",
]


def bagi(tim: list[str], seed: int) -> dict[str, str]:
    rng = random.Random(seed)
    urutan = []
    while len(urutan) < len(tim):
        putaran = KASUS[:]
        rng.shuffle(putaran)
        urutan += putaran
    return dict(zip(tim, urutan))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("tim", nargs="*", help="nama tim")
    p.add_argument("--seed", type=int, required=True, help="angka acak yang diumumkan di kelas")
    p.add_argument("--jumlah", type=int, help="jumlah tim, kalau tidak menyebut nama")
    a = p.parse_args()

    tim = a.tim or [f"Tim {i}" for i in range(1, (a.jumlah or 0) + 1)]
    if not tim:
        p.error("sebut nama tim atau pakai --jumlah")
    if len(set(tim)) != len(tim):
        p.error("ada nama tim yang sama")

    print(f"seed = {a.seed}\n")
    lebar = max(len(t) for t in tim)
    for t, k in bagi(tim, a.seed).items():
        print(f"{t:<{lebar}}  →  {k}")


if __name__ == "__main__":
    main()
