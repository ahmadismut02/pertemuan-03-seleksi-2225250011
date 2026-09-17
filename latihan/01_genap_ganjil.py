# Input: menerima satu bilangan bulat dari pengguna
# Proses: mengecek sisa hasil bagi (%) dengan 2
# Keputusan: jika sisa 0 maka genap, selain itu ganjil
# Output: menampilkan status bilangan (Genap/Ganjil)

bilangan = int(input("Masukkan bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")