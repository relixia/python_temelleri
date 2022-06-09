name = "Sadık"
surname = "Turan"
age = 36

greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old."
length = len(greeting)
#\n sayesinde bir alt satıra geçiş yapabilirsin.
print(greeting)

print(greeting[0])
print(greeting[3])

print(len(greeting))
#len sayesinde string'in kaç karakterli bir dizi olduğunu öğrenirsin.

print(greeting[length-1]) #string dizisindeki son karakteri printler (sonuç . çıkacak çünkü son karakter nokta)
print(greeting[-1]) #yukarıdaki ile aynı sonuç gelecek.

print(greeting[3:7]) #2. indeksten 5. indekse kadar printler (sonuç name çıkacak)

print(greeting[3:]) #başlangıcı belirleyip sonu belirlemezsen başlangıçtan sonuna kadar gider.
print(greeting[:16]) #sonu belirleyip başlangıcı belirlemezsen en baştan belirlediğin indekse kadar gider.

print(greeting[2:40:2]) #2. indeksten 40. indekse kadar 2'şer 2'şer printler.
