
"""
müşteri verilerini ve satın aldığı ürün bilgilerini değişkenlerde sakla 
toplam ücret nedir ?
ödenen ücretin kdv oranı nedir (%18)
"""

musteri1İsim = "Alperen Coban"
musteri1Numara = "08501234567"
musteri1Mail = "infoAlperen@gmail.com"
musteri1Sehir = "Kırklareli"

# satın alınan ürünler
kablosuzMouseFiyat = 550
kablosuzKlavyeFiyat = 650
dizUstuBilgisayarFiyat = 55000 

kdv = 1.18

toplamFiyat = kablosuzKlavyeFiyat + kablosuzMouseFiyat + dizUstuBilgisayarFiyat 
kdvliFiyat = toplamFiyat * 1.18

print("Toplam Kdvsiz Fiyat: " + str(toplamFiyat))
print("Toplam Kdvli Fiyat: " + str(kdvliFiyat))

# TypeError: can only concatenate str (not "int") to str
# Str() int değerini karakter değerine dönüştürür
