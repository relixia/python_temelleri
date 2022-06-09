#sadece konu anlatımı var, videoyu tekrar izle.
#özet: def fonksiyonu içinde def fonksiyonu dışında olan bir değişkene yeni veri atadığın zaman
#def fonksiyonu içinde atanan yani local veriye göre çalışıyor.
#ayrıca dışarıda tanımlanan değişkenin de değeri değişmiyor.
#4. satırda yazdığımın olmamasını istiyorsan videonun sonunda yazılan kodu kullan.

x = 50

def test():
    x=100
    print(x)


print(x) #sonuç 50 geliyor
test() #sonuç 100 geliyor


y = 60

def test2():
    global y #böyle yaptığın zaman fonksiyon içinde yaptığın tüm işlemler globaldeki değere atanır.
    y = 120

test2()
print(y) #sonuç 120 çıkıyor.
    
