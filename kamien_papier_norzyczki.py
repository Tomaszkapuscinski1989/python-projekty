def menu():
    menu = "Opcje".upper().center(30, "-")
    menu1 = "nowa gra".upper().ljust(28, ".")
    menu2 = "wyjscie".upper().ljust(28, ".")
    menu3 = "".center(30, "-")
    print("")
    print(menu)
    print(menu1, 1)
    print(menu2, 2)
    print(menu3)
    wyb = input(">> ")
    return wyb


wyb = menu()
while wyb != "2":
    print(22)

    wyb = menu()
