message = "Hello There. My name is Buğra Çayır"
print(message)

message = message.upper() #tüm harfleri büyük yapar.
print(message)

message = message.lower() #tüm harfleri küçük yapar.
print(message)

message = message.title() #tüm kelimelerin baş harfi büyük olur.
print(message)

message = message.capitalize() #sadece ilk kelimenin baş harfi büyük olur.
print(message)

message = " Hello There. My name is Buğra Çayır" #başta boşluk var
message = message.strip() #baştaki boşluk silindi
print(message)

message = message.split() #boşluk karakterlerine göre ayrıştırma yapar.
#Bu ayrıştırmaya göre işlemler gerçekleştirebilirsin. Örneğin 23. satıra bak
print(message)
print(message[2]) #2. indeks için My kelimesini yazdırdı.

message = "Hello There. My name is Buğra Çayır" #1. satır ile aynı
message = message.split(".") #ayrıştırma işlemini boşluklara göre değil noktalara göre yapar.
print(message)
print(message[1])

message = "Hello There. My name is Buğra Çayır" #1. satır ile aynı
message = message.split() #boşluklara ayırdık
print(message)
message = " ".join(message) #mesaj eski haline (30. satırdaki haline) geri döndü.
print(message)

message = message.split()
message = "---".join(message)
print(message)

message = "Hello There. My name is Buğra Çayır" #1. satır ile aynı
index = message.find("Buğra") #Buğra kelimesinin message'deki index başlangıcını bulur
print(index) #cevap 24 çıkacak.
#eğer yukarıdaki işlemler sonucunda cevap -1 çıkıyorsa aradığın şey aradığın yerde yoktur.

isFound = message.startswith("H") #girdiğin harfle başlayıp başlamadığını söyler.
print(isFound) #cevap True çıkacak

isFound2 = message.endswith("r") #girdiğin harfle bitip bitmediğini söyler.
print(isFound2) # cevap True çıkacak

message = message.replace("Buğra", "Erdem")
print(message)

message = message.replace(" ", "*") #boşluk karakterlerini * ile değiştirdi
print(message)

message = "Hello There. My name is Buğra Çayır" #1. satır ile aynı
message = message.replace("ı", "i").replace("ö", "o").replace("ç", "c")
print(message)

message = "Hello There. My name is Buğra Çayır" #1. satır ile aynı
message = message.center(50) #sağ ve soldan 50 karakter koyarak ortalar.
print(message)

message = "Hello There. My name is Buğra Çayır" #1. satır ile aynı
message = message.center(80, "*") #sağ ve soldan 75 karakter koyup ortalar ve oralara * yerleştirir.
print(message)
