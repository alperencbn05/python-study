# 1- Girilen 2 sayıdan hangisi büyüktür?

# sayi1 = int(input("Lutfen ilk sayiyi giriniz:"))
# sayi2 = int(input("Lutfen ikinci sayiyi giriniz:"))

# sonuc = (sayi1 > sayi2)
# mesaj = f"{sayi1} sayisi {sayi2} sayisindan büyüktür = {sonuc}"
# print(mesaj)

# 2- Girilen  bir sayının tek çift kontrolünü yapınız

# girilenSayi = int(input("Lutfen sayiyi giriniz:"))
# tekciftKontrol = ((girilenSayi % 2) == 0)
# print("Sayi çift mi " + str(tekciftKontrol))

# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstü başarılı

not1 = int(input("Lutfen ilk notunuzu giriniz:"))
not2 = int(input("Lutfen ikinci notunuzu giriniz:"))
not3 = int(input("Lutfen üçüncü notunuzu giriniz:"))

ortalamaHesap = (((not1 + not2 + not3) / 3) >= 50)
print("Gecti mi:" + str(ortalamaHesap))
