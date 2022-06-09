# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ["Bmw","Mercedes","Opel","Mazda"]
print(arabalar)

# 2-  Liste Kaç elemanlıdır ?
result1 = len(arabalar)
print(result1)

# 3-  Listenin ilk ve son elemanı nedir ?
result3İlk = arabalar[0]
print(result3İlk)

result3Son = arabalar[-1]
print(result3Son)

# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[-1]= "Toyota"
result4 = arabalar
print(arabalar)

# 5-  Mercedes listenin bir elemanı mıdır ? 
result5 = 'Mercedes' in arabalar
print(result5)

# 6-  Listenin -2 indeksindeki değer nedir ?
result6 = arabalar[-2]
print(result6)

# 7-  Listenin ilk 3 elemanını alın.
result7 = arabalar[0:3]
result7 = arabalar[:3]
result7 = arabalar[-2:]  #30, 31 ve 32. satırların hepsi aynı sonucu veriyor.
print(result7)

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ["Toyota","Renault"]
result8 = arabalar
print(result8)

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result9 = arabalar + ["Audi","Nissan"]
print(result9) #result9 listesi 6 elemanlı oldu
print(arabalar) #arabalar listesi hala 4 elemanlı

# 10- Listenin son elemanını silin.
del arabalar[-1]
result10 = arabalar
print(result10)

# 11- Liste elemanlarını tersten yazdırınız.
result11 = arabalar[::-1]
print(result11)
print(arabalar)

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

print(studentA, studentB, studentC)

# 13- Liste elemanlarını ekrana yazdırınız.

result13 = studentA[0]
print(result13)
result13 = studentB[1]
print(result13)
result13 = studentC[3][1]
print(result13)

# 14- "Yiğit Bilgi 9 yaşında ve not ortalaması 66"
result14 = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result14)