"""
    dosya açma ve oluşturmak için open() fonksiyonu kullanılır

    kullanımı               :open(dosya_adi , dosya_erişme_modu)
    dosya_erişme modu       :dosyaayı hangi amaçla açtığımızım belirtir.
    "r" okuma modu          :okuma modu,belirtilen konumda dosya olmalıdır.
    seek                    :cursor konumu      


"""
dosya = open("log.txt" , encoding="utf-8")

print(dosya.read())
dosya.seek(5)
print(dosya.read())



