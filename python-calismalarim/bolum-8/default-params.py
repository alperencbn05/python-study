def selamlama(isim  = "insan" , mesaj = "iyi günler"):
    return f"{mesaj} , {isim}"


# print(selamlama())


def toplama(a , b):
    return a + b
def cikarma(a,b):
    return a - b
def islem(a,b,fn):
    return fn(a,b)

# print(islem(14 , 25 , toplama))