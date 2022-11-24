print("Pilih menu:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
bilpertama =int(input("Masukkan angka pertama: "))
bilkedua =int(input("Masukkan angka kedua: "))
menu =input("Pilihan Anda: ")
if menu=="1" :
    tambah= bilpertama+bilkedua
    print("hasil :",tambah)
elif menu=="2" :
    kurang= bilpertama-bilkedua
    print("hasil :",kurang)
elif menu=="3" :
    kali=bilpertama*bilkedua
    print("hasil ",kali)
else:
    bagi=bilpertama/bilkedua
    print("hasil :",bagi)
