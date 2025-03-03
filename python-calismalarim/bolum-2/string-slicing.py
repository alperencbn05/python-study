kurs = "Pyhton ile Programlama"

print(kurs[0]) # p karakteri çıkar
print(kurs[-1])# a karakteri çıkar


adet = len(kurs)
print(adet)

# print(kurs[adet])
# IndexError: string index out of range

print(kurs[adet-1]) # sonuncu karaktere karşılık gelir

print(kurs[0:6])   # python'a karşılık gelir
print(kurs[:6])   # python'a karşılık gelir

print(kurs[11:adet]) # Programlama'ya karşılık gelir
print(kurs[7:]) # sonu belirtilmezse sona kadar gider

print(kurs[-11:]) # -11 den başla sona kadar git
print(kurs[0:6:2]) # 2 şer 2şer atlayarak götürür

print(kurs[::-1]) # tersten adımlar bu sayede ters cevirmis olur