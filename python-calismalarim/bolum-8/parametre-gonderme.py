def selamlama(isim):
    return "Merhaba , " +isim

# print(selamlama("Alperen"))
# print(selamlama("Mehmet"))

def toplam(sayi1 , sayi2):
    return sayi1 + sayi2

# print(toplam(5",7))

def yasHesapla(dogumYili):
    return 2025 - dogumYili


def emekliligeKacYilKaldi(dogumYili , isim):


    
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas
    if kalanSure > 0:
        return f"{isim} emekliğinize {kalanSure} yıl kaldı."
    else:
        print("Emekli olmaya hak kazandınız.")

print(emekliligeKacYilKaldi(1967 ,"Alperen"))