liste = ["1" , "3"  , "5" , "20b" , "abc" , "10a" , "60"]

# liste elemanları içindeki sayısal değerleri bulunuz

# kullanıcı q (quit) değerini girmedikçe aldığınız her elemanın sayı olduguna emin olunuz aksi takdirde hata veriniz

# for x in liste:
#     try:
#         sonuc = int(x)
#         print(x)
#     except ValueError:
#         continue

# while True:
#     try:
#         sayiGirisi = (input("sayi giriniz:(çıkmak için q): "))
#         if (sayiGirisi == "q".lower()):
#             break
#         sonuc = float(sayiGirisi)
#         print(sayiGirisi)
#         break
#     except ValueError:
#          print("Hatalı giriş yaptınız")
#          continue
    
# dictionary ve key parametle olarak alan bir dict fonksiyonu hazırlayınız 

urun = {"urunAdi" : "Samsung S24"}

def urunbulucu(liste , key):
    try:
        return liste[key]
    except KeyError:
        return None
    
print(urunbulucu(urun , "fiyat"))
    


        

