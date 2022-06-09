website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
#Lütfen aşağıdaki soruları kendiniz cevaplayınız.

# 1- "course" karakter dizisinde kaç karakter vardır?
lengthCourse = len(course)
print(lengthCourse)

# 2- 'website' içinden www karakterlerini alın.
result2 = website[7:10]
print(result2)

# 3- 'website' içinden com karakterlerini alın.
lengthWebsite = len(website)
result3 = website[lengthWebsite-3:]
print(result3)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result4_ilk15 = course[0:15]
result4_son15 = course[-15:]
print(result4_ilk15)
print(result4_son15)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result5 = course[::-1]
print(result5)

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.' 
name = "Bora"
surname = "Yılmaz"
age = 32
job = "Mühendis"

result6 = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}"
print(result6)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = "Hello world"
s = s[0:6] + "W" + s[-4:] #uzun yolu
s.replace("w", "W") #kolay yolu
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result8 = "abc" * 3
print(result8)