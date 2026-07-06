import random

# menyiapkan pilihan player dan computer
pilihan = ['gunting', 'batu', 'kertas']
input_player = input("Masukkan pilihan kamu (gunting, batu, atau kertas): ").lower()
input_computer = random.choice(pilihan)

print(f"pilihan kamu: {input_player}")
print(f"pilihan komputer: {input_computer}")