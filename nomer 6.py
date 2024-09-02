# Agar mendapat nilai B, rata-rata nilai yang harus didapat adalah 79.5
grade = input("Masukkan target Grade yang dimau : ")
min = float(input("Masukkan minimal nilai agar mendapat Grade yang dimau : "))
avg = float(input("Masukkan rata-rata nilai sekarang : "))
pers = float(input("Persentase pembobotan nilai ujian akhir : "))

# rumus 
# nilai minimal = rata-rata yang dimiliki * pembobotan + nilai yang harus didapat di exam * pembobotan exam
nilaiharus = (min - avg * (100-pers)/100) * 100 / pers


print(nilaiharus)

