# Sito Eratostenesa
import math
import time
import os


def liczby_pierwsze_metoda_1(zakres=1000):

    tablica = set([m for m in range(2, zakres + 1)])

    def gen():
        for f in range(2, round(math.sqrt(zakres)) + 1):
            for k in range(2, (zakres // 2) + 1):
                if (f * k) <= zakres and (f * k) in tablica:
                    yield f * k

    d = gen()
    for w in d:
        tablica.remove(w)

    print(len(tablica))
    print(tablica)


def liczby_pierwsze_metoda_2(zakres=1000):

    tablica = set([m for m in range(2, zakres + 1)])

    for f in range(2, round(math.sqrt(zakres)) + 1):
        for k in range(2, (zakres // 2) + 1):
            if (f * k) <= zakres and (f * k) in tablica:
                tablica.remove(f * k)

    print(len(tablica))
    print(tablica)


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


start2 = time.perf_counter()
liczby_pierwsze_metoda_1(liczba)
end2 = time.perf_counter()
print(
    f"Wyznaczenie liczb pierwszych metodą pierwszą zajeło {(end2 - start2)*1000:.3f} ms"
)


start3 = time.perf_counter()
liczby_pierwsze_metoda_2(liczba)
end3 = time.perf_counter()
print(f"Wyznaczenie liczb pierwszych metodą drugą zajeło {(end3 - start3)*1000:.3f} ms")
