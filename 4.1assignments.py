#x = 5
#y = 10
#z = 20

x, y, z = 5, 10, 20

x, y = y, x

#x, y = y, x

#x = x + 5
x += 5 #satır 11'deki işlemle aynı şey

#x = x - 5
x -= 5 #satır 14'deki işlemle aynı şey

#x = x * 5
x *= 5 #satır 17'deki işlemle aynı şey

#x = x / 5
x /= 5 #satır 20'deki işlemle aynı şey

#x = x % 5
x %= 5 #satır 23'deki işlemle aynı şey

#x = x // 5
x //= 5

#x = y ** 5
x **= 5

print(x, y, z)

values = 1, 2, 3

print(values)
print(type(values))

x, y, z = values

print(x, y, z)

values1 = 1,2,3,4,5 #x y z sadece 3 tane değer ama bu tuple'da 5 tane değer var.
x, y, *z = values1 
print(x,y,z)