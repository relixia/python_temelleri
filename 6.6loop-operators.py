# range
for item in range(2):    #range operatörü => range(10) yazabilirsin range(5,10) veya range (5,10,2) yazabilirsin.
    print(item)

# enumerate
index = 0
greeting = "Hello"

#for letter in greeting:
#    print(f"Index: {index} Letter: {letter}")
#    index += 1

#for letter in greeting:     #satır 9 - 11 ile aynı şey
#    print(f"Index: {index} Letter: {greeting[index]}")
#    index += 1

#for index,letter in enumerate(greeting):
#    print(f"Index: {index} Letter: {letter}")

for item in enumerate(greeting):    #satır 17 - 18 ile aynı şey
    print(item)
    

# zip
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1, list2)))
print(list(zip(list1, list2, list3)))

for item2 in zip(list1, list2, list3):
    print(item2)

for a,b,c in zip(list1, list2, list3):
    print(a)
