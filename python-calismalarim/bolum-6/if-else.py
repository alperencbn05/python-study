email = "info@sadikturan.com"
parola = "12345"
email = input("Eposta adresinizi giriniz: ")
parola = input("Parolanızı giriniz: ")

if(email == "info@sadikturan.com"):
    if(parola == "12345"):
        print("Giriş yapıldı.")
    else:
        print("parola yanlış")
else:
    print("email yanlış")