from db import *

def urunEkle(urunAdi , urunFiyati):
    urun = {"urunAdi": urunAdi, "urunFiyati": urunFiyati}
    urunler.append(urun)