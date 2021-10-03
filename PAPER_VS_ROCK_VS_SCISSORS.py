import random

bronie = ["K", "P", "N"]

game_on = "T"
P_1_points = 0
P_2_points = 0
while game_on == "T":

    P_1 = input("Graczu, wybierz broń(K/P/N): ")
#losowanie kompa
    P_2_index = random.randrange(0, len(bronie))
    P_2 = bronie[P_2_index]
    if P1 == "K":
        P1_bron = "KAMIEŃ"
    elif P1 == "P":
        P1_bron = "PAPIER"


    if P_1 == "K" and P_2 == "K":
        wynik = "remis..."
        print(wynik)
    elif P_1 == "K" and P_2 == "P":
        wynik = "P_2 wygrywa!!!"
        print(wynik)
    elif P_1 == "K" and P_2 == "N":
        wynik = "P_1 wygrywa!!!"
        print(wynik)
    elif P_1 == "P" and P_2 == "K":
        wynik = "P_1 wygrywa!!!"
        print(wynik)
    elif P_1 == "P" and P_2 == "P":
        wynik = "remis..."
        print(wynik)
    elif P_1 == "P" and P_2 == "N":
        wynik = "P_2 wygrywa!!!"
        print(wynik)
    elif P_1 == "N" and P_2 == "K":
        wynik = "P_2 wygrywa!!!"
        print(wynik)
    elif P_1 == "N" and P_2 == "P":
        wynik = "P_1 wygrywa!!!"
        print(wynik)
    elif P_1 == "N" and P_2 == "N":
        wynik = "remis..."
        print(wynik)

    print("...")

    if wynik == "P_1 wygrywa!!!":
        P_1_points += 1
        print(f"P_1 = {P_1_points} points; P2 = {P_2_points} points" )
    elif wynik == "P_2 wygrywa!!!":
        P_2_points += 1
        print(f"P_1 = {P_1_points} points; P2 = {P_2_points} points" )
    elif wynik == "remis...":
        print(f"P_1 = {P_1_points} points; P2 = {P_2_points} points" )

    game_on = input("Gramy dalej(T/N)?")