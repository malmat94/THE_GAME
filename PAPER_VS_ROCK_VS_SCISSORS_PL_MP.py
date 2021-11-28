import getpass
from time import sleep

def PRS_Multi_game():

    game_on = "t"
    P_1_points = 0
    P_2_points = 0
    while game_on == "t":

        P_1 = getpass.getpass(prompt = "Graczu 1, wybierz broń(K/P/N): ").upper()
        while True:
            if P_1 == "K" or P_1 == "P" or P_1 == "N":
                break
            else:
                print("Zły znak!!")
                print("")
                P_1 = getpass.getpass(prompt = "Graczu 1, wybierz broń(K/P/N): ").upper()

        P_2 = getpass.getpass(prompt = "Graczu 2, wybierz broń(K/P/N): ").upper()
        while True:
            if P_2 == "K" or P_2 == "P" or P_2 == "N":
                break
            else:
                print("Zły znak!!")
                print("")
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

        print(f""" - Gracz nr 1 wybrał: {P1_bron}
        
- Gracz nr 2 wybrał: {P2_bron}""")
        print("****************************")
        print("-------------VS-------------")
        print("****************************")

        sleep(1)

        if P_1 == "K" and P_2 == "K":
            wynik = "          remis..."
            print(wynik)
        elif P_1 == "K" and P_2 == "P":
            wynik = "     Gracz 2 wygrywa!!!"
            print(wynik)
        elif P_1 == "K" and P_2 == "N":
            wynik = "     Gracz 1 wygrywa!!!"
            print(wynik)
        elif P_1 == "P" and P_2 == "K":
            wynik = "     Gracz 2 wygrywa!!!"
            print(wynik)
        elif P_1 == "P" and P_2 == "P":
            wynik = "          remis..."
            print(wynik)
        elif P_1 == "P" and P_2 == "N":
            wynik = "     Gracz 2 wygrywa!!!"
            print(wynik)
        elif P_1 == "N" and P_2 == "K":
            wynik = "     Gracz 2 wygrywa!!!"
            print(wynik)
        elif P_1 == "N" and P_2 == "P":
            wynik = "     Gracz 1 wygrywa!!!"
            print(wynik)
        elif P_1 == "N" and P_2 == "N":
            wynik = "          remis..."
            print(wynik)

        print("____________**______________")

        if wynik == "     Gracz 1 wygrywa!!!":
            P_1_points += 1
            print(f"Gracz 1 : {P_1_points} pkt; Gracz 2 : {P_2_points} pkt" )
        elif wynik == "     Gracz 2 wygrywa!!!":
            P_2_points += 1
            print(f"Gracz 1 : {P_1_points} pkt; Gracz 2 : {P_2_points} pkt" )
        elif wynik == "          remis...":
            print(f"Gracz 1 : {P_1_points} pkt; Gracz 2 : {P_2_points} pkt" )

        game_on = input("Gramy dalej(t-tak/n-nie)?").casefold()
        while True:

            if game_on == "t" or game_on == "n":
                break
            else:
                print("Zły znak!!")
                print("")
                game_on = input("Gramy dalej(t-tak/n-nie)?").casefold()
