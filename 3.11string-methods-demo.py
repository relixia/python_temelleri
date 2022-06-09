website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result1 = " Hello World ".strip()
print(result1)
#result1 = " Hello World ".rstrip() sağdaki boşlukları silmek için
#result1 = " Hello World ".lstrip() soldaki boşlukları silmek için

anotherStripExample = website.lstrip("/:pth")
print(anotherStripExample) #cevap www.sadikturan.com olacak

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result2 = "www.sadikturan.com".strip("w.com")
print(result2)

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result3 = course.lower()
print(result3)

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result4 = website.count("a")
print(result4)

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result5Starting = website.startswith("www")
print(result5Starting)
result5Ending = website.endswith("com")
print(result5Ending)

# 6-  'website' içinde '.com' ifadesi var mı?
result6 = website.find(".com")
print(result6) #eğer varsa indeks numarasını verecek, bu sayede olup olmadığını anlarsın.
result6Example = website.find(".com",0,10) #0 ile 10 indeksi arasında .com var mı yok mu diye anlamak için
print(result6Example) #sonuç -1 olacak bu demek ki yok

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result7 = course.isalpha()
print(result7)
result7Example = course.isdigit()
print(result7)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result8 = "Contents".center(50,"*")
print(result8)
result8Example = "Contents".ljust(50, "*")
print(result8Example)
result8Example2 = "Contents".rjust(50, "*")
print(result8Example2)

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result9 = course.replace(" ", "-")
print(result9)
result9Example = course.replace(" ", "-",5) #sadece 5 kere tekrarlar bunu
print(result9Example)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result10 = "Hello World".replace("World", "There")
print(result10)

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result11 = course.split(" ")
print(result11)
