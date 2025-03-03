myList = [1,2,3]
myTuple = 1,2,3  # değiştirilemez

print(type(myList))
print(type(myTuple))

myList[0] = 2
sonuc = myList
print(sonuc)

# myTuple[0] = 2
# sonuc = myList
# print(sonuc)
# TypeError: 'tuple' object does not support item assignment

myTuple2 = tuple([1,2,3])
print(type(myTuple2))