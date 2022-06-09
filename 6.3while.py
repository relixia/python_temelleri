# 1 - 100'e kadar

x = 0

while x <= 100:
    print(x)
    x += 1
    
print("1'den 100'e kadar tüm sayılar bitti")

y = 0

while y <= 100:
    if y % 2 == 1:
        print(y)
    y += 1

print("1'den 100'e kadar tek sayılar bitti")

z = 0

while z <= 100:
    if z % 2 == 1:
        print(f"sayı tek: {z}")
    else:
        print(f"sayı çift: {z}")
    z += 1

name = "" #İçi boş olduğu için False olacak.
while not name.strip(): #true olana kadar döngüyü döndür. (.strip'in amacı boşluk karakterinin girilmesini engellemek.)
    name = input("İsminizi giriniz: ")

print(f"Merhaba, {name}")

