# bankamatik uygulamas

# Hesap bilgileri tutulcak. (dict)
#menu paraCekme paraYatırma bakiyeSorgula gibi fonksiyonlar eklenecek
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılıp kullanılmayacagı sorulcak

hesaplar = [ 
 {
"ad" : "alperen çoban",
"yaş" : "18",
"para"  : 5000,
"ekhesaptakipara": 20000,
"username" : "AlperenCbn05",
"password" : "123456"
 }
]


def menu(hesap):
    print("\n")

    print(f"Merhaba {hesap["ad"]}")

    print("1- Bakiye sorgulama")
    print("2- Para yatırma")
    print("3- Para Çekme")

    islem = input("Yapmak istediğiniz işlem (1,2,3): ")
    if islem ==  "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraYatirma(hesap)
    elif islem == "3":
        paraCekme(hesap)
    else:
        print("Yanlış tuşladınız.")
    


def login():
    username = input("username: ")
    password = input("password: ")

    isLoggedIn  = False

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break
        if not(isLoggedIn == True):
            print("username ya da password yanlış")
def bakiyeSorgula(hesap):
   print(f" Ana paranız : {hesap["para"]}")
   print(f"Ek paranız : {hesap["ekhesaptakipara"]}")
   print("\n")
   menu(hesap) 
def paraYatirma(hesap):
    yatirilcakTutar = float(int(input("Yatirmak istediğiniz tutari giriniz: ")))
    yeniPara = hesap["para"] + yatirilcakTutar
    hesap["para"] = yeniPara
    print(f"hesaptaki yeni paranız {hesap["para"]}")
    menu(hesap)
def paraCekme(hesap):
    cekilcekTutar = float(int(input("Çekmek istediğiniz tutari giriniz: ")))
    if hesap["para"] >= cekilcekTutar:
        yeniPara = hesap["para"] - cekilcekTutar
        hesap["para"] = yeniPara
        print(f"hesaptaki yeni paranız {hesap["para"]}")
        menu(hesap)
    else:
        ekHesapIstek = input(" Hesabınızdaki bakiye yetersiz. Ek hesaptan para çekmek ister misiniz(evet hayir): ").lower()
        if ekHesapIstek == "hayir":
            menu(hesap)
        else:
            cekilcekTutar = float(int(input("Çekmek istediğiniz tutari giriniz: ")))
            yeniPara = hesap["ekhesaptakipara"] - cekilcekTutar
            hesap["ekhesaptakipara"] = yeniPara
            print(f"Ek hesaptaki yeni paranız {hesap["ekhesaptakipara"]}")
            menu(hesap)



login()


    

