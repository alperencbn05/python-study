"""
    module1 (db) : urunler
    module2 (methods) : urunEkle() , urunGuncelle(),
    module3 (app)  :

    yeni ürün ekleme --> urunekle("iphone 15" , 60000)
    ürün gencelle --> urunGuncelle(" 1, "iphone 15 pro , 80000)
    ürünleri listele --> urunlerigetir()


"""

from db import *
from methods import *

urunEkle("İphone15" , "3131")