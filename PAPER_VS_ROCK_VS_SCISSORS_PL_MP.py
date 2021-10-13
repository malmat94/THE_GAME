import getpass

bronie = ["K", "P", "N"]

game_on = "t"
P_1_points = 0
P_2_points = 0
while game_on == "t":

    P_1 = getpass.getpass(prompt = "Graczu 1, wybierz broń(K/P/N): ").upper()
    P_2 = getpass.getpass(prompt = "Graczu 2, wybierz broń(K/P/N): ").upper()

    if P_1 == "K":
        P1_bron = "KAMIEŃ"
    elif P_1 == "P":
        P1_bron = "PAPIER"
    elif P_1 == "N":
        P1_bron = "NOŻYCE"

    if P_2 == "K":
        P2_bron = "KAMIEŃ"
    elif P_2 == "P":
        P2_bron = "PAPIER"
    elif P_2 == "N":
        P2_bron = "NOŻYCE"

    print(f"""Gracz nr 1 wybrał: {P1_bron}
Gracz nr 2 wybrał: {P2_bron}""")


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

    game_on = input("Gramy dalej(t/n)?").casefold()