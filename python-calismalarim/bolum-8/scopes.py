# local space
# global scope

# x = "global scope"

# def myFunc():
#     x = "local scope"
#     return x

# print(x)
# print(myFunc())

name = "Alperen"

def change_name(new_name):
    global name
    name = new_name
    return name

print(change_name("ismet"))

def greeting():
    
    name = "Alperen"

    def hello():
        name = "Ada"
        print("Hello" , name)
    hello()

greeting()