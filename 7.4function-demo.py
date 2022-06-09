
#gönderilen bir kelimeyi belirtilen kez ekrana yazdır.
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("merhaba\n", 10)

#kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
def listeyeCevir(*params):
    liste = []

    for param in params:
        liste.append(param)
    return liste

listeyeCevir(10,20,30,"merhaba")

#gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.
sayi1 = int(input("sayi 1: "))
sayi2 = int(input("sayi 2: "))

def asalSayi(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalSayi(sayi1, sayi2)

#kendisine gönderilen bir sayının tam bölenlerini bir liste haline getir.
def tamBolenleriBul(bolensayi):
    tamBolenler = []

    for i2 in range(2, bolensayi):
        if (bolensayi % i2 == 0):
            tamBolenler.append(i2)
    
    return tamBolenler


print(tamBolenleriBul(20))
