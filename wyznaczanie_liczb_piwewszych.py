# Sito Eratostenesa
import math
import time
import os


def liczby_pierwsze_metoda_1(zakres):

    tablica = set([m for m in range(2, zakres + 1)])

    z = (zakres // 2) + 1

    for f in range(2, round(math.sqrt(zakres)) + 1):
        for k in range(2, z):
            if (f * k) <= zakres and (f * k) in tablica:
                tablica.remove(f * k)

    print(len(tablica))


os.system("cls" if os.name == "nt" else "clear")
while True:
    try:

        liczba = int(
            input(
                "Podaj ostatnią liczbę zakresu dla którego chcesz wyznaczyć liczby pierwsze:\n>> "
            )
        )
    except ValueError:
        os.system("cls" if os.name == "nt" else "clear")
        print("podaj liczbę".upper())
    else:
        break

lista2 = []
for x in range(11):
    start2 = time.perf_counter()
    liczby_pierwsze_metoda_1(liczba)
    end2 = time.perf_counter()
    print(f"{x} Wyznaczenie liczb pierwszych zajeło {(end2 - start2)*1000:.3f} ms")
    lista2.append((end2 - start2) * 1000)


print(f"średnio {sum(lista2)/len(lista2):.3f} ms")
