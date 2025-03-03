# bir aracın yakıt tipine göre (benzin , dizel , lpg) belirtilen bir mesafede ne kadar yakıt masrafı
# olduğunu hesaplayan uygulamayı yapınız.
# benzin = 39.35
# dizel 41.71
# lpg 20.28

# benzin = 39.35 # 1 ltlerin fiyati
# dizel =  41.71
# lpg =  20.28

# ortalamaYakitTuketimi = float(input("100 kmde harcanan ortalama yakıt miktarini giriniz: "))
# yakitTipi = input("Aracinizin yakit tipini giriniz: ").lower()
# gidilecekYol = float(input("Gidilen mesafeyi giriniz: "))

# harcananYakit = gidilecekYol * (ortalamaYakitTuketimi / 100)

# if(yakitTipi == "benzin"):
#     sonuc = harcananYakit * 39.35
#     print("Masrafiniz: " + str(sonuc))
# elif(yakitTipi == "dizel"):
#     sonuc = harcananYakit * 41.71
#     print("Masrafiniz: " + str(sonuc))
# else:
#     sonuc = harcananYakit * 20.28
    # print("Masrafiniz: " + str(sonuc))


# bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayın ve hesaplanan ortalamaya göre karşılık gelen
# not aralığını bulunuz

# 0-24 = 0
# 25-44 = 1
# 45 - 54 = 2
# 55-69 = 3
# 70-85 = 4
# 85-100 = 5

not1 = int(input("İlk notunuzu giriniz: "))
not2 = int(input("İkinci notunuzu giriniz: "))
not3 = int(input("Sözlü notunuzu giriniz: "))
  
OrtalamaNot = (not1 + not2 + not3) / 3

if(OrtalamaNot < 24) and (OrtalamaNot >= 0):
    print("Notunuz 5 üzerinden 0 dir")
elif(OrtalamaNot < 44) and (OrtalamaNot >= 25):
    print("Notunuz 5 üzerinden 1 dir")
elif(OrtalamaNot < 54) and (OrtalamaNot >= 45):
    print("Notunuz 5 üzerinden 2 dir")
elif(OrtalamaNot < 70) and (OrtalamaNot >= 55):
    print("Notunuz 5 üzerinden 3 dir")
elif(OrtalamaNot < 85) and (OrtalamaNot >= 70):
    print("Notunuz 5 üzerinden 4 dir")
elif(OrtalamaNot < 100) and (OrtalamaNot >= 85):
    print("Notunuz 5 üzerinden 5 dir")
else:
    print("Notunuzu yanlış veya eksik girdiniz.")
