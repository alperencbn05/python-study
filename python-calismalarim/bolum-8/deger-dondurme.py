def toplam():
    return 10+20

# sonuc = toplam()
# print(sonuc)

# def yasHesapla ():
#     return 2025-dogumYili

# dogumYili = 2006

# print(yasHesapla())

def saat():
    import datetime
    return datetime.datetime.now().hour
def selamlama():
    if (saat() < 12):
        return "Günaydın"
    else:
        return "iyi akşamlar"
print(selamlama())
