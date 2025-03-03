sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız
# for x in sayilar:
#     print(x)

#2- "sayilar" listesindeki hangi sayılar 3' ün katıdır?
# for x in sayilar:
#     if(x % 3 == 0):
#         print(x)

# 3- "sayilar" listesindeki tüm sayıların toplamı nedir

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam)

urunler  = ["samsung s24" , "samsung s22" , "iphone 15" , "iphone 14"]

# # 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz

# for urun in urunler:
#     iphone = urun.find("iphone")
#     if iphone > -1:
#         print(urun)
    
# 5- "urunler" listesinde kaç tane samsung marka telefon vardır

adet = 0
for urun in urunler:
    index = urun.find("samsung")
    if (index > -1):
        adet += 1
print(adet)    