# class
class Product:
    def __init__(self , name , price , isActive) :
       self.name = name
       self.price = price
       self.isActive = isActive
    # method
    # attribute , property



# Instance, Object =  Nesne

p1 = Product("Iphone 15 pro max" , 50000 , True)
p2 = Product("Samsung pro" , 3529  , True)
1
sonuc = p1.name
sonuc2 = p2.price
print(sonuc)
print(sonuc2)

urunler = [p1 , p2]

for urun in urunler:
    if urun.isActive == True:
        print(f"ürün adı:{urun.name} ürün fiyat:{urun.price}")

