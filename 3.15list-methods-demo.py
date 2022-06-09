names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
# names.insert(len(names), 'Mehmet') #en sona ekleme yapmak için
print(names)

# 3-  "Deniz" isminin indeksi nedir ?
index  = names.index('Deniz')
print(index)
# names.pop(index) #Deniz ismini listeden silmek için

# 4-  "Deniz" ismini listeden siliniz.
names.remove('Deniz')
# names.pop()
print(names)

# 5-  "Ali" listenin bir elemanı mıdır ?
result5 = 'Ali' in names
print(result5) #eğer listedeyse True değerini veriyor.
result5 = names.index('Ali')
print(result5) #eğer index bilgisi -1'den farklıysa demek ki listenin bir elemanıdır.

# 6-  Liste elemanlarını ters çevirin.
result6 = names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
result7 = names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
result8 = years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result9 = str.split(',')
print(result9)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
min = min(years)
print(min)

max = max(years)
print(max)

# 11- years dizisinde kaç tane 1998 değeri vardır ?
result11 = years.count(1998)
print(result11)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka1 = input("Birinci marka: ")
markalar.append(marka1)

marka2 = input("İkinci marka: ")
markalar.append(marka2)

marka3 = input("Üçüncü marka: ")
markalar.append(marka3)

print(markalar)