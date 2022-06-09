x, y, z = 2, 5, 10

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?

a = int(input('1.sayı: '))
b = int(input('2.sayı: '))

result1 = (a * b) - (x+y+z)
print(result1)

# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
result2 = y // x
print(result2)

# 3- (x,y,z) toplamının mod 3' ü nedir ?

toplam = (x+ y+ z)
result3 = toplam % 3
print(result3)

# 4- y' nin x. kuvvetini hesaplayınız.
result4 = y ** x
print(result4)

# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result5 = z ** 3
print(result5)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?

numbers = 1, 5, 7, 10, 6
x, *y ,z = numbers

result6 = y[0] + y[1] + y[2]
print(result6)
