# pertama-tama masukkan angka

height = float(input("masukkan tinggi bendungan dalam satuan meter : "))
flow = float(input("masukkan jumlah debit air : "))


# 1 kubik sama dengan 1000 kilogram
#konstanta gravitasi 9.8 m/s^2
#flow sebesar 1300

massa = 1000 * flow

konstanta_Gravitasi = 9.8

# w sebagai simbol usaha

w = massa * konstanta_Gravitasi * height

#kita ubah dari Watt menjadi MegaWatt
Mw = w / 10**6

print("total usaha yang dihasilkan oleh bendungan : ", w )

#efisiensi dilambangkan dengan lambang e

e = Mw * 0.9
print("total listrik yang dihasilkan oleh bendungan : ", e)