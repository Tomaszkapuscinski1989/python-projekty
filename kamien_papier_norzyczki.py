def menu():
    wyb = 0
    while wyb != 1 and wyb != 2:
        menu = "Opcje".upper().center(30, "-")
        menu1 = "nowa gra".upper().ljust(28, ".")
        menu2 = "wyjscie".upper().ljust(28, ".")
        menu3 = "".center(30, "-")
        print("")
        print(menu)
        print(menu1, 1)
        print(menu2, 2)
        print(menu3)

        try:
            wyb = int(input(">> "))
            if wyb < 1 or wyb > 2:
                raise ValueError
        except ValueError:
            print("hfkshfdk")
            continue

    return wyb


wyb = menu()
while wyb != 2:
    print(22)

    wyb = menu()
