# # 1 "Toyota , Bmw , Renault , Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
# markalar = ["Toyota" , "Bmw" , "Renault" , "Mercedes"]
# # liste kaç elemanlıdır
# print(len(markalar))
# # listenin ilk ve son elemanı nedir
# print(markalar[0]+" "+markalar[-1])
# #4- "Renault markasını" "Togg" ile güncelleyiniz.
# markalar[2] = "Togg"
# print(markalar)
# # Togg listenin bir elemanı mıdır?
# # varMi = "Togg" in markalar
# # print(varMi)
# # listenin ilk iki elemanını alınız.
# # sonuc = markalar[0:2]
# # print(sonuc)
# # Listenin sonuna ford ve citroen ekleyiniz
# sonuc = markalar + ["Ford", "Citroen"]
# print(sonuc)
# #listenin son elemanını siliniz.
# del(sonuc[-1])
# print(sonuc)

# aşağıdaki verileri liste içerisinde saklayınız
  # ogrenci1: Yigit bilgi 2010[70 , 80 ,90]
  # ogrenci2: Ada   bilgi 2011[70 , 70 ,90]
  # ogrenci2: Çınar Turan 2013[70 , 100 ,90]

ogrenci1 = ["Yigit","Bilgi",2010,70,80,90]
ogrenci2 = ["Ada","Bilgi",2011,70,70,90]
ogrenci3 = ["Cinar","Turan",2013,70,100,90]

ogrenciler = ["ogrenci1","ogrenci2","ogrenci3"]

# ogrenci1Yas = 2025 - ogrenci1[2]
# ogrenci2Yas = 2025 - ogrenci2[2]
# ogrenci3Yas = 2025 - ogrenci3[2]

# ogrenciYaslar = [ogrenci1Yas , ogrenci2Yas ,ogrenci3Yas]
# print(ogrenciYaslar[0])

ogrenciNotlar = ogrenci1[3:] + ogrenci2[3:] + ogrenci3[3:]

print(sum(ogrenciNotlar)/9)
