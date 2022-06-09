x = 5
hak = 5
devam = "e"

result = 5 < x < 10
print(result)
#yukarıdaki kodların problemi: yukarıdaki kod 2 sorudan oluşuyor:
#x 5'ten büyük mü? x 10'dan küçük mü?
#bir tanesi bile sağlanmasa cevap false gelebilir ve hangisinin sağlanmadığını bilemeyiz.

#and
#True, False => False
#True, True => True
#False, False => False
result1 = (x > 5) and (x < 10) #true true ise cevap True'dur
result2 = (hak > 0) and (devam == "e") #oyuncu oyuna devam edebilir.

print(result1)
print(result2)

#or => and'de iki şeyin de doğruluğuna bakıyorduk, burada sadece bir tanesinin doğruluğu bizim için önemli
#True, False => True
#True, True => True
#False, False => False
result3 = (x > 0) or (x % 2 == 0)
print(result3)

#not
result4 = not(x > 0)
print(result4)


# x, 5 ile 10 arasında olan bir çift sayı mı?
result5 = ((x > 5) and (x < 10)) and (x % 2 == 0)
print(result5)