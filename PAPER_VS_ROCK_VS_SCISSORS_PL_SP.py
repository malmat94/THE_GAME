import random
from time import sleep

def PRS_Single_game():

    bronie = ["K", "P", "N"]

    game_on = "t"
    P_1_points = 0
    P_2_points = 0
    while game_on == "t":

        P_1 = input("Graczu, wybierz broń(K/P/N): ").upper()
        while True:

            if P_1 == "K" or P_1 == "P" or P_1 == "N":
                break
            else:
                print("Zły znak!!")
                print("")
                P_1 = input("Graczu, wybierz broń(K/P/N): ").upper()

    #losowanie kompa
        P_2_index = random.randrange(0, len(bronie))
        P_2 = bronie[P_2_index]
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
        print("")
        print(f""" - Wybrałeś: {P1_bron}

 - Komputer wybrał: {P2_bron}""")
        print("****************************")
        print("-------------VS-------------")
        print("****************************")

        sleep(1)

        if P_1 == "K" and P_2 == "K":
            wynik = "          remis..."
            print(wynik)
        elif P_1 == "K" and P_2 == "P":
            wynik = "     Wygrał komputer..."
            print(wynik)
        elif P_1 == "K" and P_2 == "N":
            wynik = "        Wygrałeś!!!"
            print(wynik)
        elif P_1 == "P" and P_2 == "K":
            wynik = "        Wygrałeś!!!"
            print(wynik)
        elif P_1 == "P" and P_2 == "P":
            wynik = "          remis..."
            print(wynik)
        elif P_1 == "P" and P_2 == "N":
            wynik = "     Wygrał komputer..."
            print(wynik)
        elif P_1 == "N" and P_2 == "K":
            wynik = "     Wygrał komputer..."
            print(wynik)
        elif P_1 == "N" and P_2 == "P":
            wynik = "        Wygrałeś!!!"
            print(wynik)
        elif P_1 == "N" and P_2 == "N":
            wynik = "          remis..."
            print(wynik)

        print("____________**______________")

        if wynik == "        Wygrałeś!!!":
            P_1_points += 1
            print(f"Gracz = {P_1_points} pkt; Komputer = {P_2_points} pkt" )
        elif wynik == "     Wygrał komputer...":
            P_2_points += 1
            print(f"Gracz = {P_1_points} pkt; Komputer = {P_2_points} pkt" )
        elif wynik == "          remis...":
            print(f"Gracz = {P_1_points} pkt; Komputer = {P_2_points} pkt" )
        print("")

        game_on = input("Gramy dalej(t-tak/n-nie)?").casefold()
        while True:

            if game_on == "t" or game_on == "n":
                break
            else:
                print("Zły znak!!")
                print("")
                game_on = input("Gramy dalej(t-tak/n-nie)?").casefold()



