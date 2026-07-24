import random

def main():
    print("=" * 40)
    print(" 🎮 GAME BATU, GUNTING, KERTAS 🎮 ")
    print("=" * 40)

    # daftar pilihan yang tersedia
    pilihan = ["gunting", "batu", "kertas"]

    # input dari pemain
    pemain = input("Masukkan pilihan Anda (gunting, batu, kertas): ").lower().strip()

    # jika pemain tidak memilih salah satu dari pilihan yang tersedia
    if pemain not in pilihan:
        print("Pilihan tidak valid. Silahkan pilih gunting, batu, atau kertas!")
        return
    
    # pilihan komputer secara acak
    komputer = random.choice(pilihan)
    