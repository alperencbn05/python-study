isim = "Alperen Çoban"

# for harf in isim:
#     if (harf == "o"):
#         break
#     print(har

sayi = 0
sayilar = []

while (sayi<100):
    sayi += 1
    if(sayi % 2 == 1):
        continue
    sayilar.append(sayi)

for sayi in sayilar:
    print(sayi)