def changeName(n):
    n = "Ada"

name = "Buğra"

changeName(name)
print(name) #cevap Buğra olmaya devam etti yani Ada diye değişmedi
 
'''
def change(n):
    n[0] = "İstanbul"

sehirler = ["Ankara", "İzmir"]

change(sehirler)
print(sehirler) #yukardakinin aksine burda bir değişim gerçekleşti
'''

def change(n):
    n[0] = "İstanbul"

sehirler = ["Ankara", "İzmir"]
n = sehirler[:] #slicing yaptık

n[0] = " istanbul"

print(sehirler)
print(n) #atama yaptığımız için bu sefer farklı çıktılar

change(sehirler[:])
print(sehirler)

def add(a, b, c = 0):
    return sum((a,b,c))

print(add(10,20))
#eğer 3 parametre vermek istiyorsak fonksiyona c ekliyoruz:
print(add(10,20,30))

#daha fazla parametre vermek istiyorsak böyle tek tek c d e falan eklemiyoruz:

def addversion2(*params):
    print(params) #tuple olarak tüm girdileri yazdırabiliyoruz
    print(params[1]) #girdilerden indeks seçebiliyoruz
    return sum(params)

print(addversion2(10,20,30,10,10,10)) #istediğim kadar ekliyorum

#fonksiyonda sum fonksiyonunu kullanmak istemezsek:
def addversion3(*params):
    sum = 0
    for n in params:
        sum = sum + n
    return sum

print(addversion3(10,20,30,10,10,10))

def displayUser(**args): #args yerine params yazılabilir. ** olmasının sebebi dictionary geleceğini bildirmek
    for key, value in args.items():
        print("{} is {}".format(key,value))

displayUser(name = "Bugra", age = 18, city = "Erzurum")
displayUser(name = "Buse", age = 7, city = "Erzurum", phone = 2523)
displayUser(name = "Sevim", age = 40, city = "İstanbul", phone = 2523, mail = "mail@hotmail.com")

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1 = "value 1", key2 = "value 2")