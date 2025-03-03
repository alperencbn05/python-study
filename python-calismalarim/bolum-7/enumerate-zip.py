markalar = ["opel" , "bmw" , "citroen"]
# index = 1

# for marka in markalar:
#     print(f"{index} - {marka}")
#     index += 1

# obj1 = enumerate(markalar)
# print(type(obj1))
# print(list(obj1))

# for index,marka in enumerate(markalar, 1):
#     print(f"{index}-{marka}")

# zip metodu

numara = [100,200,300]
ogrenci = ["Ali", "Ayşe" , "Canan" , "Mehmet"]

print(list(zip(numara , ogrenci)))

for ogr in zip(numara,ogrenci):
    print(ogr)