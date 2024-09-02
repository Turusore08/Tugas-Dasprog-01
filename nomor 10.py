x1 = float(input("Masukkan x1 :"))
y1 = float(input("Masukkan y1 :"))
x2 = float (input("Masukkan x2 :"))
y2 = float(input("Masukkan y2 : "))

gradien = (y2-y1)/(x2-x1)
xtengah = (x2+x1)/2
ytengah = (y2+y1)/2
gradien_TL = -1/gradien
b= ytengah - gradien_TL * xtengah  # dari rumus y = mx + b

print("Titik 1 : (", x1 ,",", y2 , ")")
print("Titik 1 : (", x2 ,",", y2 , ")")
print("persamaan garis tersebut adalah y = ", gradien_TL,"x +", b )