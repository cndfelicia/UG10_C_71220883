Bulan =int(input("Masukkan bulan (1-12):"))
if Bulan ==1 or Bulan ==3 or Bulan ==5 or Bulan ==7 or Bulan ==8 or Bulan ==10 or Bulan ==12:
    print("Jumlah Hari: 31")
elif Bulan ==4 or Bulan ==6 or Bulan ==9 or Bulan ==11:
    print("Jumlah Hari: 30")
else:
    print("Jumlah Hari: 28")
