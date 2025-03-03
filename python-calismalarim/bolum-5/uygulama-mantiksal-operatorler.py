# 1- yaşı 18 den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz

# yas = int(input("Yaşınız:"))
# velc = ((yas > 18) or (veliIzni == "evet"))
# veliIzni = (input("Veli izniniz var mı ( evet ya da hayır ) : "))

# sonu# print("Calisabilir: " + str(sonuc))

# 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırın
# notunuz = int(input("Notunuz: "))
# sonuc = ((notunuz >=50) and (notunuz <= 100))
# mesaj = f"notunuz {notunuz} ve dersi geçtiniz : {sonuc}"
# print(mesaj) 

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
# zayifKontrol = (input("Zayıfınız varmı ( evet ya da hayır ) : "))
# notOrtalmasi = int(input("Not ortalamaniz: "))

# sonuc = ((notOrtalmasi >= 70) and not(zayifKontrol == "evet"))
# print("Belge alabilir:" + str(sonuc) )

# işe girmek için en az  önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu

# sigaraKontrol = (input("Sigara kullanıyor musunuz ( evet ya da hayır ) : "))
# lisansKontrol = (input("önlisans mezunu musunuz: "))
# lisansKontrol2 = (input("lisans mezunu musunuz: "))

# sonuc = ((lisansKontrol == "evet") or (lisansKontrol2 == "evet")) and not (sigaraKontrol == "evet")

# print("Başvurabilir: " + str(sonuc))

# uygulamaya giriş kontrolü username ya da email kontrolü yapalım
# username = "alperen1"
# password = "123456"
# email = "alperen@hotmail.com"
 

# emailOrUser = (input("Kullanıcı adınızı ve ya Emailinizi giriniz: "))
# kullaniciPassword = (input("Şifrenizi giriniz: "))

# sonuc = ((emailOrUser == username) or (emailOrUser == email)) and (password == kullaniciPassword)
# print("Uygulamaya giriş yapabilir: " + str(sonuc))