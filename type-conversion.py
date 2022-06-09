""""
x = input("1. sayı: ")
y = input("2. sayı: ")

print(type(x))
print(type(y))

toplam = int(x) + int(y)

print(toplam)
"""
# başa ve sona 3 tane çift tırnak atmak arasındaki her şeyi comment haline getirir.

x = 5
y = 2.5
name = "Çınar"
isOnline = True

#Type Conversion

#int to float
x = float(x)
print(x) #cevap 5.0 olacak
print(type(x)) 

#float to int
y = int(y)
print(y) #cevap 2 olacak
print(type(y))

result = x + y
print(result)
print(type(result))

#bool to str (str = string demek)
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

#bool to int
isOnline = int(isOnline)
print(isOnline) #cevap 1 olacak çünkü True 1 olarak çevriliyor. False olsaydı 0 olacaktı
print(type(isOnline))

