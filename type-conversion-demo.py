"""
yarıçapı verilen bir dairenin alanını ve çevresini hesapla.
area = pi r^2
circumference = 2 pi r
"""

pi = 3.14
radius = float(input("radius: "))
area = pi * (radius ** 2)
circumference = 2 * pi * radius

print("Area: ", area)
print("Circumference: ", circumference)

print("Area " + str(area) + " Circumference: " + str(circumference))
