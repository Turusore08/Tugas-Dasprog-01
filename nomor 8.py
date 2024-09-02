penduduk = int(input("Masukkan jumlah penduduk : "))
# setelah mengetahui jumlah penduduknya, saatnya kita mencari jumlah toiletnya

toilet = penduduk / 3

#sekarang kita mencari penggunaan air dalam sehari

air = toilet * 15 * 14
cost = 150

#15 dari penggunaan air toilet sekali siram 14 dari penggunaan toilet sehari

penghematan = 15 - 2 

air_baru = toilet * penghematan * 14
total_hemat = air - air_baru

print("penggunaan air sehari adalah",air,"liter/hari")
print("penggunaan air sehari setelah pemasangan toilet baru adalah",air_baru,"liter/hari")
print("penghematan dalam sehari adalah",total_hemat)
print("Total biaya yang dikeluarkan adalah", toilet * cost,"$")
