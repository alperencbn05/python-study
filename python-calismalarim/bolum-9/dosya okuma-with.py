file = open("log.txt" , encoding="utf-8")


# file.close()
try:
    with open("log.txt" , encoding="utf-8") as file:
        print(file.read())
        # for i in file:
        #     print(i , end="")
except FileNotFoundError as e:
    print("dosya okuma hatası")

