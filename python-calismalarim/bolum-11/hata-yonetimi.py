
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
    except ZeroDivisionError as e:
        print("y sıfır olamaz")
        print(e)
    except ValueError as e:
        print("x ve y sayı olmalıdır")
    except:
        print("Bilinmeyen bir hata oluştu")
    else:
        break
    finally:
        print("finally blogu calıştı")