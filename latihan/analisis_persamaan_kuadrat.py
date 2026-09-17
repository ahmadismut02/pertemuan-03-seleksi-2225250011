import math

# Input: koefisien a, b, dan c (float)
# Proses: hitung D = b^2 - 4ac, lalu evaluasi akar berdasarkan nilai D
# Keputusan: nested if untuk a == 0, D > 0, D == 0, dan D < 0
# Output: jenis akar dan nilai numerik akarnya (2 angka di belakang koma)

print("Analisis Persamaan Kuadrat")
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b**2 - 4*a*c
    print(f"Diskriminan: {diskriminan:.2f}")

    if diskriminan > 0:
        x1 = (-b + math.sqrt(diskriminan)) / (2*a)
        x2 = (-b - math.sqrt(diskriminan)) / (2*a)
        print("Dua akar real berbeda:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    elif diskriminan == 0:
        x = -b / (2*a)
        print("Satu akar real kembar:")
        print(f"x = {x:.2f}")
    else:
        print("Tidak ada akar real (akar imajiner).")