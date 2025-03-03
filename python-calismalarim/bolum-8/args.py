def toplam(a,b):
    return a + b

# print(toplam(15 , 623))

# sayilar = (10,20,30,40)

# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

# sonuc = toplam(sayilar)

# print(sonuc)


# def  toplam(*args):
#     print(args)
#     sonuc = 0
#     for i in args:
#         sonuc += i
#     return args

# sonuc = toplam(10,20,50,60)

# print(sonuc)


# sayilar = (10,20,30,40)

# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

# print(toplam(sayilar))

def toplam(*args):
    print(args)
    print(type(args))
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(10,50,250))


