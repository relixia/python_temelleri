name = "Bugra Cayir"

for letter in name:
    if letter == "a":
        break
    print(letter)

for letter in name:
    if letter == "i":
        continue
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

y = 0
while y < 5:
    y += 1
    if y == 2:
        continue
    print(y)

# 1 - 100'e kadar tüm sayıların toplamı?
z = 0
result = 0
while z <= 100:
    result += z
    z += 1

print(f"1'den 100'e kadar tüm sayıların toplamı: {result}")

# 1 - 100'e kadar çift sayıların toplamı?
a = 0
result2 = 0
while a <= 100:
    a += 1
    if a % 2 == 1:
        continue
    result2 += a

print(f"1'den 100'e kadar çift sayıların toplamı: {result2}")

# 1 - 100'e kadar tek sayıların toplamı?
b = 0
result3 = 0
while b <= 100:
    b += 1
    if b % 2 == 0:
        continue
    result3 += b

print(f"1'den 100'e kadar tek sayıların toplamı: {result3}")