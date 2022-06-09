list = [1, 2, 3]

tuple = (1, "iki", 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ["ali", "veli"]
tuple = ["damla", "ayşe", "ayşe"]
print(list)
print(tuple)

list[0] = "Ahmet"
print(list)

#tuple[0] = "Deniz" #bunu yazarsan hata alırsın. Tek bir eleman üzerinde değişiklik yapamazsın

print(tuple.count("ayşe"))
print(tuple.index("ayşe"))

list = ["ali", "veli"]
tuple = ["damla", "ayşe", "ayşe"]
names = ["demet", "emel", "ayşe"] + tuple

print(names)

#tuple ve liste aynı şeyler diyebiliriz.
#tek farkları tuple tek bir eleman üzerinde değişiklik, silme işlemi yapmaya izin vermiyor.