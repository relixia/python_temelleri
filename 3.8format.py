name = "Çınar"
surname = "Turan"
age = 36

print("My name is {} {}".format(name, surname))
print("My name is {0} {1}".format(name, surname)) #4. satırdaki kod ile aynı sonucu verecek.
print("My name is {1} {0}".format(name, surname)) #Ad Soyad yerine Soyad Ad yazacak.

print("My name is {n} {s}".format(n=name, s=surname)) #4. satıdaki kod ile aynı sonucu verecek.

print("My name is {} {} and I'm {} years old.".format(name, surname, "36"))
print("My name is {} {} and I'm {} years old.".format(name, surname, age)) #11. satırdaki kod ile aynı sonucu verecek.

print("My name is {} {} and I'm {} years old.".format(name, name, name)) #her süslü parantez yerine name bilgisini yazacak.

result = 200/700
print("The result is {}".format(result)) #tüm decimal place'leri yazıyordu

print("The result is {r:1.3}".format(r=result)) #1.3 bilgisi sıfırdan önce ve sonra kaç decimal place olacağını belirtiyor.
print("The result is {r:1.5}".format(r=result))

print(f"My name is {name} {surname} and I'm {age} years old.") #11. satırdaki kod ile aynı sonucu verecek fakat daha kolay ve temiz bir yöntem.
