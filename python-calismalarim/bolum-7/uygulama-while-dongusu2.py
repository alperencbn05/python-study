# # 1- klavyeden girilen n sayıdaki çğrenci bilgisini liste içerisinde saklayınız.
# # ** dictionary listesi yapısı (ogrenciNo , ogrenciAdi , ogrenciSoyad) şeklinde olsun.
# # ** ürün ekleme işlemi bittiğinde öğrencileri listeleyiniz.

# ogrenciListesi = []

# n = int(input("Kaç öğrenci gireceksiniz:"))


# for i in range(n):
#     ogrenciNo = input(f"{i+1}. Öğrencinin numarasını girin: ")
#     ogrenciAdi = input(f"{i+1}. Öğrencinin adını girin: ")
#     ogrenciSoyad = input(f"{i+1}. Öğrencinin soyadını girin:")

#     ogrenci = {
#     'ogrenciNo': ogrenciNo,
#     'ogrenciAdi': ogrenciAdi,
#     'ogrenciSoyad': ogrenciSoyad }

#     ogrenciListesi.append(ogrenci)

# for ogrenci in ogrenciListesi:
#     print(f"Öğrenci Numarası: {ogrenci['ogrenciNo']}, Adı: {ogrenci['ogrenciAdi']}, Soyadı: {ogrenci['ogrenciSoyad']}")
    

# # 1- klavyeden girilen n sayıdaki çğrenci bilgisini liste içerisinde saklayınız.
# # ** dictionary listesi yapısı (ogrenciNo , ogrenciAdi , ogrenciSoyad) şeklinde olsun.
# # ** ürün ekleme işlemi bittiğinde öğrencileri listeleyiniz.

ogrenciListesi = []


n = int(input("Kaç öğrenci gireceksiniz:"))
i = 0
while i < n :
    ogrenciNo = input(f"{i+1}. Öğrencinin numarasını girin: ")  
    ogrenciAdi = input(f"{i+1}. Öğrencinin adını girin: ")
    ogrenciSoyad = input(f"{i+1}. Öğrencinin soyadını girin:")
    i += 1

    ogrenci = { 'ogrenciNo': ogrenciNo,
             'ogrenciAdi': ogrenciAdi,
            'ogrenciSoyad': ogrenciSoyad }
    
    ogrenciListesi.append(ogrenci)
print(ogrenciListesi)

