# not uygulaması

# 1- Menu
    # 1- Not gir
    #2- Ortalaması Göster(90-100 --> AA 85-89 --> 5,4,3,2,1 şeklinde yapıcam ben)
    #3- Notları kayıt et
    #4-çıkış


import sys
ogrenciAdi = ""
not1 = 0
not2 = 0


def kayitliSonuclar ():
    global ogrenciAdi, not1, not2
    with open("notlar.txt" , "r" , encoding="utf-8") as file:
        print(file.read())
        file.seek(0)

    



def  kayitEt():
    while True:
        with open("notlar.txt" , "a" , encoding="utf-8") as file :
            ogrenciAdi = input("Adınızı ve Soyadınızı giriniz: ")
            not1 = int(input("ilk notu giriniz:"))
            not2 = int(input("ikinci notu giriniz:"))
            ortalamaNot = (not1 + not2) / 2
            if (ortalamaNot>=85 and ortalamaNot<=100):
                yeni_kayit = f"{ogrenciAdi} {ortalamaNot} Notunuz : 5\n"
            elif(ortalamaNot>=70 and ortalamaNot<=84):
                yeni_kayit = f"{ogrenciAdi} {ortalamaNot} Notunuz : 4\n"
            elif(ortalamaNot>=55 and ortalamaNot<=69):
                yeni_kayit = f"{ogrenciAdi} {ortalamaNot} Notunuz : 3\n"
            elif(ortalamaNot>=45 and ortalamaNot<=54):
                yeni_kayit = f"{ogrenciAdi} {ortalamaNot} Notunuz : 2\n"
            elif(ortalamaNot>=0 and ortalamaNot<=44):
                yeni_kayit = f"{ogrenciAdi} {ortalamaNot} Notunuz : 1\n"
            else:
                print("Yanlış not girdiniz.")  
                continue
            file.write(yeni_kayit)

        print("\neklenen kayit:")
        print(yeni_kayit)

        with open("direktnotlar.txt" , "a" , encoding="utf-8") as file:
            ogrenciAdNot = F"{ogrenciAdi} : {not1} , {not2}"
            file.write(ogrenciAdNot)

        devam = input("Başka bir kullanıcı girmek istiyor musunuz? (evet,hayir): ").lower()
        if devam == "hayir":
            menu()     
def menu():
    print("1-Not kayıt et:")
    print("2-Kayıtlı notlara bak:")
    print("3-çıkış yap")

    tercih = input("Ne yapmak istersiniz(1,2,3): ")

    if tercih == "1":
        kayitEt()
    elif tercih == "2":
        kayitliSonuclar()
    elif tercih == "3":
        cikisYap()
    else:
        print("Yanlış bir şey girdiniz")

def cikisYap():
    print("Çıkış yapılıyor...")
    sys.exit()




menu()