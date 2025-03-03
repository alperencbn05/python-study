# # faktöriyel fonksiyonu oluşturunuz ve fonksiyona
# # gelen değerlerde hata varsa hata mesajı fırlatın

# def faktoriyel(sayi):
#     try:
#         if not isinstance (sayi ,(int , float)):
#         if (sayi != int(sayi)):
#              raise ValueError("Geçersiz karakter girdiniz.")
#         if (sayi < 0):
#               raise Exception("Negatif sayıların faktöriyeli yoktur.")
        

#         sonuc = 1
#         for i in range(1 , sayi+1):
#             sonuc *= i
#         return sonuc

#     except ValueError as ve:
#         return(str(ve))
#     except Exception as ee:
#         return(str(ee))


    

          

import re
        




# print(faktoriyel(a))
    
# 2-) Girilen parola içinde türkçe karakter varsa hata veriniz

def parola(sifre):
    sifre = str(sifre)
    if re.search(r"[çğıİöşü]", sifre) is not None:
        raise NameError("Şifre hatalıdır, Türkçe karakter içeremez.")
    
    return "sifre geçerli"


print(parola("aç"))
