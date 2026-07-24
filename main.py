import random

print("=" * 50)
print(" 🎮 GAME BATU, GUNTING, KERTAS 🎮 ")
print("=" * 50)

 # daftar pilihan yang tersedia
pilihan = ["gunting", "batu", "kertas"]

# input dari pemain
while True:
    pemain = input("Masukkan pilihan Anda (gunting, batu, kertas): ").lower().strip()
    if pemain not in pilihan:
        print("Pilihan tidak valid. Silahkan pilih gunting, batu, atau kertas!")
    else:
        break
    
# pilihan komputer secara acak
komputer = random.choice(pilihan)

# pilihan pemain dan komputer
print(f"\nPilihan Anda: {pemain}")
print(f"Pilihan Komputer: {komputer}")

# menentukan pemenang
if pemain == komputer:
    hasil = "Hasil SERIII!"
elif(pemain == "gunting" and komputer == "kertas") or \
        (pemain == "batu" and komputer == "gunting") or \
        (pemain == "kertas" and komputer == "batu"): 
    hasil = "Kamu MENANG!"
else:
    hasil = "Kamu KALAH!"
print(f"\nHasil: {hasil}")