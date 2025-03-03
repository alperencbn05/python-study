# open (dosya_adi,dosya_erişim_modu)
# dosya erişim modu --> dosyayı hangi amaçla açtığımızı belirtir

# "r" : (Read) okuma. Dosya konumda yoksa hata verir
# "w" : (Write) yazma modu
#   ** dosyayı konumda oluşturur
#   ** dosya içeriğini siler ve yeniden ekleme yapar
# "a" : (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+" : Hem okuma hem yazma modunda açılır.Dosya konumda yoksa
# hata verir


with open("dosya.txt" , "r+" , encoding="utf-8" ) as file:
    # file.seek(0) a modunda bir işe yaramaz
    # file.seek(1)
    file.read()
    file.write("ikinci satır\n")
