#value (değer) type => string, number
x = 5
y = 25

x = y

y = 10

print(x,y)

#reference types => list
#reference types'da adres değişikliği yapılıyor.
a = ["apple", "banana"]
b = ["apple", "banana"]

a = b

b[0] = "grape"

print(a, b)