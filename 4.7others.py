# Identity operator: is

x = y = [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z) #line 6 ve 7'de referans karşılaştırması yaptık, True geldi

print(x is y) #adres karşılaştırması yapıyoruz, x ve y aynı adreste o yüzden True gelecek.
print(x is z) #adres karşılaştırmasına göre x ve z aynı değerlere sahip olsa da farklı adreslere sahip bu yüzden False gelecek.

x = [1,2,3]
y = [2,4]

print(x==y)
print(x is y)

del x[2]
y[1] = 1 
y.reverse() #line 17 18 ve 19'daki işlemlerle x ve y liste içeriklerini birebir aynı yaptık.

print(x==y)
print(x is y)
print(x is not y)

#Membership operator: in

x = ["apple", "banana"]
print("banana" in x) #true gelecek

name = "Bugra"
print("a" in name)
print("a" not in name)
