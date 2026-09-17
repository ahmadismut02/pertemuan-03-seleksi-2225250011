# Input: nilai akhir (float) dan kehadiran (float)
# Proses: mengecek dua kondisi sekaligus dengan operator 'and'
# Keputusan: nilai >= 60 DAN kehadiran >= 80% untuk lulus
# Output: status "Lulus" atau "Belum lulus"

nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")