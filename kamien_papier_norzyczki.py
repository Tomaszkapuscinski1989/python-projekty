import os
import random

score = {"win": 0, "lost": 0, "tie": 0}
fig = ["Kamień", "Papier", "Nożyczki"]


def menu():
    option = {
        "quit": 2,
        "play": 1,
    }
    wyb = 0

    while not (wyb in option.values()):

        print("")
        print("Opcje".upper().center(30, "-"))
        print("nowa gra".upper().ljust(28, "."), option["play"])
        print("wyjscie".upper().ljust(28, "."), option["quit"])
        print("".center(30, "-"))

        try:
            wyb = int(input(">> "))
            if not (wyb in option.values()):
                raise ValueError
        except ValueError:
            os.system("cls" if os.name == "nt" else "clear")
            print("błedny wybór\nwybierz ponownie".upper())

        else:
            os.system("cls" if os.name == "nt" else "clear")

    return wyb


os.system("cls" if os.name == "nt" else "clear")
wyb = menu()
while wyb != 2:
    os.system("cls" if os.name == "nt" else "clear")
    comp = random.choice(fig)

    move = True
    while move:
        try:
            player = input("Twój wybór:\nkAMIEŃ\npAPIER\nnOŻYCZKI\n>> ")
            if player == "k":
                player = fig[0]
            elif player == "p":
                player = fig[1]
            elif player == "n":
                player = fig[2]
            else:
                raise ValueError
        except ValueError:
            os.system("cls" if os.name == "nt" else "clear")
            print("błedny wybór\nwybierz ponownie".upper())
        else:
            move = False
            os.system("cls" if os.name == "nt" else "clear")

    if (
        (player == fig[0] and comp == fig[2])
        or (player == fig[1] and comp == fig[0])
        or (player == fig[2] and comp == fig[1])
    ):
        print(f"Gracz wybrał: {player}")
        print(f"Konputer wybrał: {comp}")
        print("wygrałeś".upper())
        score["win"] += 1
    elif player == comp:
        print(f"Gracz wybrał: {player}")
        print(f"Konputer wybrał: {comp}")
        print("remis".upper())
        score["tie"] += 1
    else:
        print(f"Gracz wybrał: {player}")
        print(f"Konputer wybrał: {comp}")
        print("przegrałeś".upper())
        score["lost"] += 1
    wyb = menu()

else:
    print(
        f'Wyniki gry:\nwygrane: {score["win"]}\nprzegrane: {score["lost"]}\nremisy: {score["tie"]}'.upper()
    )
