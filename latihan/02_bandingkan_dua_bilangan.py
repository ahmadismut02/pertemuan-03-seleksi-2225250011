# Input: menerima dua bilangan float
# Proses: membandingkan 'a' dan 'b' menggunakan nested if
# Keputusan: cek apakah a > b, jika tidak cek apakah a == b
# Output: pesan perbandingan (lebih besar, lebih kecil, atau sama)

a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

if a >= b:
    if a == b:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar.")
else:
    print("Bilangan pertama lebih kecil.")