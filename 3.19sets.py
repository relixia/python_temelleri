fruits = {"orange", "apple", "banana"}

#print(fruits[0]) #indekslenemez.
#sıralayamıyoruz (büyükten küçüğe gibi)

for x in fruits:
    print(x)
#indekslenemediği için bu şekilde tüm elemanlarını yazdırabiliriz.

fruits.add("cherry")
fruits.update(["mango", "grape","apple"]) #.add ile aynı şey
#apple zaten içinde vardı, birebir aynı şeyleri ikinci kere eklemez.

print(fruits)

fruits.remove("mango")
fruits.discard("apple") #.remove ile aynı şey

print(fruits)

fruits.pop() #listelerde son elemanı siliyordu çünkü listeler sıralıydı, fakat setler sıralı değil

print(fruits)

fruits.clear() #her şeyi temizler

print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList)) #yukarıdaki listedeki tekrarlayan elemanlar listeden çıkarılır.
