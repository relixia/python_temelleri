def sayHello(name = "user"):
    print("Hello " + name)

sayHello("Buğra") #herhangi bir listeye erişmeden yazılıyor. mesela list.sayHello() demiyoruz.
sayHello("Buse")
sayHello()


def sayHello2(name = "user"):
    return "Hello " + name

msg = sayHello2("Buğra")
print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

ageBugra = yasHesapla(2003)
print(ageBugra)

def emekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kaç yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emeklisiniz.")

emekliligeKacYilKaldi(2003, "Bugra")

print(help(emekliligeKacYilKaldi)) #girdiğimiz ''' şeklindeki yorum satırlarındaki bilgileri aktarır
                                #fonksiyonun nasıl kullanılacağını kullanıcıya anlatır.

list = [1,2,3]

print(help(list.append))

