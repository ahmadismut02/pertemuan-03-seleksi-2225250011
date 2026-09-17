# Pertemuan 03 Seleksi Python

Nama: Ahmad Ismut Thoriequddin
NIM: 2225250011
Kelas: 3A

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. Menerima input koefisien a, b, dan c dalam bentuk float dari pengguna.
2. Memeriksa apakah nilai a sama dengan 0. Jika ya, tampilkan bahwa input bukan persamaan kuadrat.
3. Jika a tidak sama dengan 0, hitung nilai diskriminan dengan rumus D = b^2 - 4ac.
4. Memeriksa nilai diskriminan menggunakan nested if:
   - Jika D > 0, hitung dua akar real berbeda (x1 dan x2) lalu tampilkan hasilnya.
   - Jika D == 0, hitung satu akar real kembar (x) lalu tampilkan hasilnya.
   - Jika D < 0, tampilkan pesan bahwa persamaan tidak memiliki akar real.
5. Menampilkan seluruh hasil kalkulasi dengan pembulatan 2 angka di belakang koma.

## Hasil Pengujian
| Input (a, b, c) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- |
| a = 0, b = 2, c = 1 | Bukan persamaan kuadrat. | Bukan persamaan kuadrat. | Berhasil |
| a = 1, b = -5, c = 6 | D = 1.00, Akar real berbeda: x1 = 3.00, x2 = 2.00 | D = 1.00, Akar real berbeda: x1 = 3.00, x2 = 2.00 | Berhasil |
| a = 1, b = -4, c = 4 | D = 0.00, Akar real kembar: x = 2.00 | D = 0.00, Akar real kembar: x = 2.00 | Berhasil |
| a = 1, b = 2, c = 5 | D = -16.00, Tidak ada akar real. | D = -16.00, Tidak ada akar real. | Berhasil |

## Refleksi
Kesalahan logika yang sempat ditemukan adalah lupa menyertakan pengecekan awal untuk `a == 0`. Jika nilai `a` bernilai 0 dan program langsung menghitung rumus diskriminan atau pembagian akar, akan timbul kesalahan matematis karena pembagian dengan angka nol (`ZeroDivisionError`) pada rumus akar. Cara memperbaikinya adalah dengan menempatkan pengecekan `if a == 0:` di struktur paling luar sebelum menghitung diskriminan.