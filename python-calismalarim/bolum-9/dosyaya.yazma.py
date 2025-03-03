# w : (write) yazma modu


with open("dosya.txt" , "w" , encoding="utf-8") as file:
    file.write("Alperen Çoban\n")
    file.write("Fenerbahçe\n")

with open("dosya.txt" , "r" , encoding="utf-8") as file:
    print(file.read())