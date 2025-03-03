# def display_user(*args):
#     print(type(args))                    # tuple
#     print(args)

# display_user()


def displayUser(**kwargs):  
    for plaka,sehir in kwargs.items():
        print(f"{plaka} : {sehir} " )
    print("\n")


displayUser(plakod = "39" , sehir = "kırklareli")
