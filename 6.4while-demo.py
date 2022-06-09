from typing import cast


sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))

while baslangic < bitis:
    baslangic += 1
    if baslangic % 2 == 1:
        print(baslangic)

#ders çözümü:
# i = baslangic
# while i < bitis:
#     i += 1
#     if (i % 2 == 1):
#         print(i)

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

i3 = 100
while i3 > 0:
    print(i3)
    i3 -= 1

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

numbers4 = []
i4 = 0
while i4 < 5:
    sayi4 = int(input('sayı: '))
    numbers4.append(sayi4)
    i4 += 1
numbers4.sort()
print(numbers4)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))
i5 = 0

while(i5 < adet):
    name5 = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name5,
        'price': price
    })
    i5 += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')

