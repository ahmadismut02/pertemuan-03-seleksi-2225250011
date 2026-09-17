# Input: tiga panjang sisi segitiga (a, b, c)
# Proses: validasi syarat segitiga (a+b>c, a+c>b, b+c>a), lalu cek jenisnya dengan nested if
# Keputusan: sama sisi (a=b=c), sama kaki (dua sisi sama), atau sembarang
# Output: jenis segitiga atau pemberitahuan bukan segitiga

a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga sama sisi")
    else:
        if a == b or a == c or b == c:
            print("Segitiga sama kaki")
        else:
            print("Segitiga sembarang")
else:
    print("Ketiga sisi tidak membentuk segitiga")