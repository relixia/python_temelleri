numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
print(val)

val = max(numbers)
print(val)

val = max(letters)
print(val)

val = min(letters)
print(val)

val = numbers[3:6]
print(val)
val = numbers[:3]
print(val)

numbers[4] = 40
print(numbers)

numbers.append(49) #append ile en sona ekleme yaparsın
print(numbers)

numbers.insert(3, 78) #insert ile bir indeksin yerine istediğin sayıyı eklersin.
#not: insert ile 3. indekse 78 yazdırırken 3. indeksteki sayı silinmez, 4. indeks olur.
print(numbers)

numbers.insert(-1, 51)
print(numbers)

#numbers.pop() #bu komut ile listenin en sonundaki sayıyı silersin.
#numbers.pop(0) #bu komut ile listenin en başındaki sayıyı silersin.

#numbers.remove(49) #bu komut ile listedeki 49 sayısını silersin.

numbers.sort() #liste sayısal olarak sıralanır.
letters.sort() #liste alfabetik olarak sıralanır.
print(numbers)
print(letters)

numbers.reverse() #listeyi ters çevirir, baştan sona değil sondan başa olarak sıralanır.
letters.reverse()
print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10)) #listede kaç tane 10 olduğunu sayıyor.
print(letters.count("a")) #listede kaç tane a olduğunu sayıyor.

numbers.clear() #diziyi boşaltır.
print(numbers)