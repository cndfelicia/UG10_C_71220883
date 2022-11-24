a =input("Masukkan daftar pesanan :")
b = a.title()
print("Daftar Pesanan :",b.split(","))
c =input("Masukkan pesanan yang ingin ditambahkan :")
d = c.upper()
if c in a:
    print(d,"sudah berada dalam daftar pesanan.")
else:
    print("Hasil penambahan pada daftar pesanan :",d.split(","))
