kec = int(input("Masukkan kecepatan Pesawat (KM/H) : "))
jarak = int(input("Masukkan jarak landasan (meter) : "))

#ubah dari km/h ke m/s
kec2 = round(kec*1000/3600,2)
#mengubah rumus percepatan dari chatgpt a = v^2/2s
aks = round(kec2**2 / (2*jarak),2)
waktu= round(kec2 / aks,2)

print ("kecepatan air jet adalah : ", kec2, "m/s")
print ("akselerasi pada air jet tersebut adalah :", aks , "m/s^2")
print ("waktu yang dibutuhkan air jet untuk take of :", waktu , "second")