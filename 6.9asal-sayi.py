'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
'''

kullaniciSayi = int(input("Lütfen bir sayı giriniz: "))

asalMi = True

if kullaniciSayi == 1:
    asalMi = False

for i in range(2, kullaniciSayi):
    if kullaniciSayi % i == 0:
        asalMi = False
        break

if asalMi:
    print(f"Girdiğiniz {kullaniciSayi} sayısı asaldır.")
else:
    print(f"Girdiğiniz {kullaniciSayi} sayısı asal değildir.")
