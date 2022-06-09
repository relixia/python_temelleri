'''
    1 - 100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''

# hiç yardım almadan kendi yaptığım çözüm:

import random

secilenSayi = random.randint(1,100)
dongu = 0
kullaniciTahmini = []
hak = int(input("Kaç hakkınız olsun?: "))
can = hak


while secilenSayi != kullaniciTahmini:
    dongu += 1
    kullaniciTahmini = int(input("Tahmin ettiğiniz sayıyı giriniz: "))
    if secilenSayi == kullaniciTahmini:
        print(f"Tebrikler! Doğru sayıyı {dongu}. denemede buldunuz. Toplam puanınız: {(100 - ((100/can) * (dongu-1)))}")
    elif secilenSayi < kullaniciTahmini:
        print("Seçtiğiniz sayı çok büyük.")
    elif secilenSayi > kullaniciTahmini:
        print("Seçtiğiniz sayı çok küçük")
    hak -= 1
    print(f"Kalan hakkınız: {hak}")
    if hak <= 0 and secilenSayi != kullaniciTahmini:
        print(f"Maalesef doğru sayıyı bulamadan tüm haklarınız bitti. Doğru sayı: {secilenSayi}")
        break

'''
# ders çözümü:
import random
sayi = random.randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz?: "))
hakDers = can
sayac = 0

while hakDers > 0:
    hakDers -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - ((100 / can) * (sayac-1))}")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if hakDers == 0:
        print(f"Hakkınız bitti. Tutulan sayı {sayi}")

'''