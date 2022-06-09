from unittest import result


def square(num): return num ** 2

numbers = [1,3,5,9,10]

#bir fonksiyonun içine liste koymak için kullanılan kod:

result = list(map(square, numbers))

print(result)

#diğer yol (ama üstteki daha iyi):
for item in map(square, numbers):
    print(item)

#bu iki örnekten anlayacağın üzere "map" metodunun ya liste haline ya da for döngüsü içinde kullanılması şart.

#eğer sadece tek kullanımlık bir fonksiyon istiyorsan def ile bu fonksiyonu yapmana gerek yok:

result2 = list(map(lambda num2: num2 ** 2, numbers))
print(result2)

#buna başka bir alternatif:
alternatif = lambda num3: num3 ** 2
result3 = list(map(alternatif, numbers))
print(result3)

#istediğin özelliğe göre filterlama:
def checkEven(num4): return num4 % 2 == 0

result4 = list(filter(checkEven, numbers))
print(result4)

#buna alternatif:
result5 = list(filter(lambda sayi: sayi % 2 == 0, numbers))
print(result5)

#fonksiyon yapmak için illa def kullanmak zorunda değilsin:
check_even = lambda sayi2: sayi2 % 2 == 0

