"""
** bankaHesabi isminde bir sınıf tanımlayınız

** üretilen her bir nesne "hesapSahibi" isminde bir özelliğe
sahip olmalıdır. bankaHesabi("Alperen Çoban")

""üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup
başlangıçta 0.0 değerinde olmalıdır

**üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak
miktar bilgisini alıp bakiye üzerine ekleyin ve bakiye miktarina geri döndürün.

**Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek
miktar bilgisini alıp bakiye değerinden çıkarıp geriye döndürün

    hesap = BankaHesabi("Alperen Çoban")
    hesap.hesapSahibi --> Alperen Çoban
    hesap.bakiye --> 0.0
    hesap.paraYatir(1000) --> 1000.0
    hesap.paraCek(500) --> 500.0

"""

class bankAccount:
    def __init__(self , hesapSahibi , bakiye):
       self.hesapSahibi = hesapSahibi
       self.bakiye = float(bakiye) 

    def paraYatir(self):
        yatirilcakPara = float(input("Lütfen Yatırmak istediğiniz tutarı giriniz:"))
        self.bakiye += yatirilcakPara
        return self.bakiye
    
    def paraCek(self):
        cekilcekPara = 0
        if self.bakiye >= cekilcekPara:
            cekilcekPara = float(input("Lütfen Çekmek istediğiniz tutarı giriniz:"))
            self.bakiye -= cekilcekPara
        else:
            print("Yeterli bakiyeniz bulunmamaktadır")
        return self.bakiye

ziraat = bankAccount("Alperen Çoban", 500)

print(ziraat.paraCek())




