numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

names = ["buğra", "çınar", "sadık"]

for name in names:
    print(f"my name is {name}")


name = "Buğra Çayır"

for n in name:
    print(n) #bunun sonucunda buğra çayır harf harf tek tek yazılacak.

tuple = (1,2,3,4,5)

for t in tuple:
    print(t)

tuple2 = [(1,2), (1,3), (3,5), (5,7)]

for t2 in tuple2:
    print(t2)

for a,b in tuple2:
    print(a) #sadece 1 1 3 5 yazılacak.

d = {"k1":1, "k2":2, "k3":3}

for item in d:
    print(item) #sadece key bilgileri olan k1 k2 k3 yazdırıldı.

for item2 in d.items():
    print(item2) #eleman gruplarının tamamına ulaşıyoruz => ("k1":1) ("k2":2) ("k3":3) yazdırılacak.

for key,value in d.items(): #EN GÜZEL YOL BU
    print(key,value)
    print(key)
    print(value)

