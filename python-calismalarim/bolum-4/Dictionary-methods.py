# Dictionary metotları
# yemekTarifleri =  { 
#  "yemek1" : {
# "yemekAdi":"Musakka",
# "yemekTarifi":"tarif aciklamasi",
# "resim":"1.jpg"
# }, 
# "yemek2" :{
# "yemekAdi":"Musakka",
# "yemekTarifi":"tarif aciklamasi",
# "resim":"1.jpg"
# }, 
# "yemek3" :{
# "yemekAdi":"Musakka",
# "yemekTarifi":"tarif aciklamasi",
# "resim":"1.jpg"
# } 
# } 


# print(yemekTarifleri["yemek1"]["yemekAdi"])  



yemek1 = {
"yemekAdi":"Musakka",
"yemekTarifi":"tarif aciklamasi",
"resim":"1.jpg"
}
# access items
sonuc = yemek1.get("yemekAdi")
sonuc = yemek1.keys()
sonuc = yemek1.values()
sonuc = yemek1.items()

#uptade items
yemek1.update({"yemekAdi" : "Manti"})
print(yemek1)

# # delete items
# yemek1.pop("Yemekadi")
# yemek1.popitem()