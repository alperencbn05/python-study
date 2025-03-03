# aşağıdaki öğrenci belgelerini dictionary veri yapısında saklayınız
# 101 yiğit bilgi 2010 (40 ,50 ,60)
# 102 Ada bilgi 2012   (60 ,55 ,60)
# 103 Çınar turan 2017 (45 ,90 ,80)

# Klavyeden girilen öğrenci numarasına göre örmek cümleyi yazdırınız
    # 101 numaralı öğrenci yigit bilgi ismindeki öğrencinin  yaşı 14 ve ortalaması 70 


ogrenciler = {
   101 : {
       "Ad" :  "Yigit",
       "Soyad" : "Bilgi",
       "Dogumyili" : 2010,
       "Notlar" : [40 , 50 , 60]
       },
       
  102: { "Ad" : "Ada",
       "Soyad"  : "Bilgi",
       "Dogumyili" : 2012,
       "Notlar" : [60 , 55 , 60]
       },
   103: {
       "Ad" : "Çınar",
       "Soyad" : "Turan",
       "Dogumyili" : 2017,
       "Notlar" : [45 , 90 , 80] 
       }
}

ogrenciNo = int(input("ogrenci no giriniz: "))
ogrenci = ogrenciler[ogrenciNo]
ortalama = (ogrenci['Notlar'][0] + ogrenci['Notlar'][1] +ogrenci['Notlar'][2]) / 3





mesaj = f"{ogrenciNo} numarali öğrenci {ogrenci['Ad']} {ogrenci['Soyad']} ismindeki öğrencinin yaşı {2025 - ogrenci['Dogumyili']} ve ortalaması {ortalama} dır. "

print(mesaj)