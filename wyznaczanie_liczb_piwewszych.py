# Sito Eratostenesa
import math
import time
import os
import multiprocessing


def liczby_pierwsze_metoda_1(zakres=1000):

    tablica = set([m for m in range(2, zakres + 1)])

    def gen(tablica, zakres):
        f = 2
        while True:

            if f < round(math.sqrt(zakres)) + 1:
                k = 2
                while True:

                    if k < ((zakres // 2) + 1):
                        if (f * k) <= zakres and (f * k) in tablica:

                            yield f * k
                        k += 1
                    else:
                        break
            else:
                break
            f += 1

    d = gen(tablica, zakres)
    while True:
        try:
            tablica.remove(next(d))

        except StopIteration:
            break

    print(len(tablica))


def liczby_pierwsze_metoda_2(zakres):

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


def proces1():
    start2 = time.perf_counter()
    liczby_pierwsze_metoda_1(liczba)
    end2 = time.perf_counter()
    print(
        f"Wyznaczenie liczb pierwszych metodą pierwszą zajeło {(end2 - start2)*1000:.3f} ms"
    )


def proces2():
    start3 = time.perf_counter()
    liczby_pierwsze_metoda_2(liczba)
    end3 = time.perf_counter()
    print(
        f"Wyznaczenie liczb pierwszych metodą drugą zajeło {(end3 - start3)*1000:.3f} ms"
    )


p1 = multiprocessing.Process(target=proces1)
p2 = multiprocessing.Process(target=proces2)

p1.start()
p2.start()
