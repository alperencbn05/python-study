urunler = [
    {"urunAdi" :"Hp Victus" , "fiyat" : 32999},
    {"urunAdi" :"Lenovo Thinkpad" , "fiyat" : 25499},
    {"urunAdi" :"Apple Macbook" , "fiyat" : 49999},
    {"urunAdi" :"Huawei Matebook" , "fiyat" : 26999},
    {"urunAdi" :"Casper Nirvana" , "fiyat" : 29000},
]

# 1- aşağıdaki örnek cümleyi tüm ürünlere uygulayınız
# "Hp Victus marka ürünün fiyati 32999 Türk lirasi"

# for urun in urunler:
#     print(f"{urun["urunAdi"]} marka ürünün fiyati {urun["fiyat"]} Türk lirasi")


# 2- ürünlerin fiyat toplamı nedir.
# sonuc = 0 
# for urunfiyat in urunler:
#     sonuc += urunfiyat["fiyat"]
# print(sonuc)
        
# 3- 25000 ile 40000 arasındaki ürünleri listeyiniz.
# for urun in urunler:
#     if((urun["fiyat"] >= 25000 ) and (urun["fiyat"] <= 40000)):
#         print(urun)
    

# # 4- kullanıcıdan alınan anahtar kelimeye göre listeleyiniz
# kelime = input("Aramak istediğiniz modeli giriniz: ")
# for urun in urunler:
#    if kelime in urun["urunAdi"].lower():
#         print(f"{urun["urunAdi"]} parası {urun["fiyat"]}")
    
kelime = input("Aramak istediginiz bilgisayari giriniz: ")
for urun in urunler:
    if kelime in urun["urunAdi"].lower():
        print(f"{urun['urunAdi']} bilgisayarın fiyatı {urun["fiyat"]} dır.")