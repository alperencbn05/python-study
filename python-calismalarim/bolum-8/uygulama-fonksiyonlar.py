# 1- kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız
def mesaj(cumle ,kackez):
    for i in range(kackez):  # Döngü belirtilen sayıda döner
        print(cumle)  # Ekrana yazdırır

# mesaj("naber world", 16)  # Fonksiyonu çağır

# dikdörtgenin alan ve çevresini hesaplayan bir fonksiyon yazınız
# def alanVeCevreHesap(kenar1 , kenar2):
#     alan = kenar1 * kenar2 
#     cevre = 2 * (kenar1 + kenar2)
#     print(f"{alan} alan {cevre} çevre")
#     return

# print(alanVeCevreHesap(7,4))

#  yazı tura uygulaması yapınız fonksiyon kullanarak (random modulu)
def yaziTura():
    liste = ["yazı" , "tura"]
    import random
    return random.choice(liste)

# print(yaziTura())


# kendisine gönderilen 2 sayı arasındaki asal sayıları bul


 # 5- kendisine gönderilen bir sayının tam bölenlerini liste şeklinde yazan bir fonksiyon

def tamBolenYazan(sayi):
    tamBolenListe = []
    for i in range(1 , sayi+1):
        if (sayi % i == 0):
            tamBolenListe.append(i)
    return tamBolenListe

# print(tamBolenYazan(37))

# kendisine göderilen 2 sayı arasındakı asal sayıları bul


def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
            for i in range(2 , sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

print(asalSayilariBul(15,90))

