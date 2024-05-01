Kod = 56


def Code(num):
    pass


def code2(*args):
    print(args)
    lista2 = []
    lista3 = []

    for x in args:
        for z in args:
            for u in args:

                lista2.append(int(x + z + u))

    print(lista2)

    print(lista3)
    for y in lista2:
        if y == Kod:
            print(y)
            break


lista = []
print("Wprowadz znane Ci liczby:\nq - zakończ wprowadzanie")
while True:
    k = input(">>")
    if k == "q":
        break
    lista.append(k)


code2(*lista)
