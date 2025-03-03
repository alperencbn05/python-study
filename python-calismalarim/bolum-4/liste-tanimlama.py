programlamaDilleri = ["Python", "C#", "Java", "Javascript"]

sonuc = programlamaDilleri
# sonuc = programlamaDilleri[0:2]
# sonuc = programlamaDilleri[-1:]


#güncelleme
programlamaDilleri[-1]= "Php"

sonuc = len(programlamaDilleri)

sonuc = programlamaDilleri + ["Go", "Delphi"]

# sonuc = "python" in programlamaDilleri
# sonuc = "React" in programlamaDilleri        # koşul ifadeleri

del(programlamaDilleri[0])

for dil in programlamaDilleri:
    print(dil)

print(sonuc)