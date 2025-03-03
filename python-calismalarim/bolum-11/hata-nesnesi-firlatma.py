# print (10 / 0 )

# x = 10

# if x > 5:
#     raise Exception("x 5 den büyük olamaz")



def renklendir(text , renk):
    renkler = ("blue" , "green" ,"yellow" , "red")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır")
    if type(text) is not str:
        raise TypeError("renk str tipinde olmalıdır")
    if renk not in renkler:
        raise ValueError("Geçersiz bir renk")
    

    print(f" {text} = {renk} ")

renklendir("merhaba" ,"yellow")