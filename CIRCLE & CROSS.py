import GAME_LANGUAGE_CHOICE #import pliku z wyborem języka

language = GAME_LANGUAGE_CHOICE.choose_language("KOLKO VS KRZYZYK", "CROSS VS CIRCLE") #wybór języka, zwrot zmiennej language

A1 = " "
A2 = " "
A3 = " "
B1 = " "
B2 = " "
B3 = " "
C1 = " "
C2 = " "
C3 = " "
def game_table():
    print("      1     2     3")
    print(" ")
    print(f"A     {A1}  |  {A2}  |  {A3}")
    print("     ----|-----|----")
    print(f"B     {B1}  |  {B2}  |  {B3}")
    print("     ----|-----|----")
    print(f"C     {C1}  |  {C2}  |  {C3}")

print(" ")

right_choice = False #wybór symbolu PL
while right_choice != True:
    if language == "PL":
        P_1_symbol = input("Graczu nr 1, wybierz swój symbol (O/X): ")
        if P_1_symbol == "O":
            P_2_symbol = "X"
            right_choice = True
            print(" ")
            print(f"""Gracz nr 1 -> {P_1_symbol}
Gracz nr 2 -> {P_2_symbol}""")
        elif P_1_symbol == "X":
            P_2_symbol = "O"
            right_choice = True
            print(" ")
            print(f"""Gracz nr 1 -> {P_1_symbol}
Gracz nr 2 -> {P_2_symbol}""")
        else:
            right_choice = False
            print(" ")
            print("Zly wybor, sproboj ponownie!")
    else: #wybór symbolu ENG
        P_1_symbol = input("Player 1, choose Your symbol (O/X): ")
        if P_1_symbol == "O":
            P_2_symbol = "X"
            right_choice = True
            print(" ")
            print(f"""Player 1 -> {P_1_symbol}
Player 2 -> {P_2_symbol}""")
        elif P_1_symbol == "X":
            P_2_symbol = "O"
            right_choice = True
            print(" ")
            print(f"""Player 1 -> {P_1_symbol}
Player 2 -> {P_2_symbol}""")
        else:
            right_choice = False
            print(" ")
            print("Bad choice, try again!")

game_table()
print(" ")
if language == "PL":
    P1_choice = " "
    P2_choice = " "
    game_over = False
    while game_over != True:
        free_spot = False #Flaga dla pętli sprawdzającej, czy lokacja jest zajęta
        while free_spot != True: #Pętla sprawdząjąca, czy lokacja jest zajęta
            P1_raw_choice = input(f"Graczu nr 1 ({P_1_symbol}), wybierz pozycje: ")
            if P1_raw_choice == "A1" and A1 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "A2" and A2 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "A3" and A3 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "B1" and B1 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "B2" and B2 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "B3" and B3 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "C1" and C1 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "C2" and C2 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "C3" and C3 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            else:
                print("Zajęte!!")
                free_spot = False

        if P1_choice == "A1":
            A1 = P_1_symbol
        elif P1_choice == "A2":
            A2 = P_1_symbol
        elif P1_choice == "A3":
            A3 = P_1_symbol
        elif P1_choice == "B1":
            B1 = P_1_symbol
        elif P1_choice == "B2":
            B2 = P_1_symbol
        elif P1_choice == "B3":
            B3 = P_1_symbol
        elif P1_choice == "C1":
            C1 = P_1_symbol
        elif P1_choice == "C2":
            C2 = P_1_symbol
        elif P1_choice == "C3":
            C3 = P_1_symbol
        game_table()

        if A1 == P_1_symbol and A2 == P_1_symbol and A3 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif B1 == P_1_symbol and B2 == P_1_symbol and B3 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif C1 == P_1_symbol and C2 == P_1_symbol and C3 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif A1 == P_1_symbol and B1 == P_1_symbol and C1 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif A2 == P_1_symbol and B2 == P_1_symbol and C2 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif A3 == P_1_symbol and B3 == P_1_symbol and C3 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif A1 == P_1_symbol and B2 == P_1_symbol and C3 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif A3 == P_1_symbol and B2 == P_1_symbol and C1 == P_1_symbol:
            game_over = True
            print("Gracz 1 wygrywa!!!")
        elif A1 != " " and A2 != " " and A3 != " " and B1 != " " and B2 != " " and B3 != " " and C1 != " " and C2 != " " and C3 != " ":
            game_over = True
            print("Remis...")
        else:
            game_over = False

        if game_over == True:
            break
        else:
            game_over

        free_spot = False  # Flaga dla pętli sprawdzającej, czy lokacja jest zajęta
        while free_spot != True:  # Pętla sprawdząjąca, czy lokacja jest zajęta
            P2_raw_choice = input(f"Graczu nr 2 ({P_2_symbol}), wybierz pozycje: ")
            if P2_raw_choice == "A1" and A1 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "A2" and A2 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "A3" and A3 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "B1" and B1 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "B2" and B2 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "B3" and B3 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "C1" and C1 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "C2" and C2 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            elif P2_raw_choice == "C3" and C3 == " ":
                P2_choice = P2_raw_choice
                free_spot = True
            else:
                print("Zajęte!!")
                free_spot = False

        if P2_choice == "A1":
            A1 = P_2_symbol
        elif P2_choice == "A2":
            A2 = P_2_symbol
        elif P2_choice == "A3":
            A3 = P_2_symbol
        elif P2_choice == "B1":
            B1 = P_2_symbol
        elif P2_choice == "B2":
            B2 = P_2_symbol
        elif P2_choice == "B3":
            B3 = P_2_symbol
        elif P2_choice == "C1":
            C1 = P_2_symbol
        elif P2_choice == "C2":
            C2 = P_2_symbol
        elif P2_choice == "C3":
            C3 = P_2_symbol
        game_table()
        game_over = False

        if A1 == P_2_symbol and A2 == P_2_symbol and A3 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif B1 == P_2_symbol and B2 == P_2_symbol and B3 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif C1 == P_2_symbol and C2 == P_2_symbol and C3 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif A1 == P_2_symbol and B1 == P_2_symbol and C1 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif A2 == P_2_symbol and B2 == P_2_symbol and C2 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif A3 == P_2_symbol and B3 == P_2_symbol and C3 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif A1 == P_2_symbol and B2 == P_2_symbol and C3 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif A3 == P_2_symbol and B2 == P_2_symbol and C1 == P_2_symbol:
            game_over = True
            print("Gracz 2 wygrywa!!!")
        elif A1 != " " and A2 != " " and A3 != " " and B1 != " " and B2 != " " and B3 != " " and C1 != " " and C2 != " " and C3 != " ":
            game_over = True
            print("Remis...")
        else:
            game_over = False

else:

    game_on = "Y"
    while game_on == "Y":

        P1_choice = input("Player 1, choose Your position: ")
        if P1_choice == "A1":
            A1 = P_1_symbol
        elif P1_choice == "A2":
            A2 = P_1_symbol
        elif P1_choice == "A3":
            A3 = P_1_symbol
        elif P1_choice == "B1":
            B1 = P_1_symbol
        elif P1_choice == "B2":
            B2 = P_1_symbol
        elif P1_choice == "B3":
            B3 = P_1_symbol
        elif P1_choice == "C1":
            C1 = P_1_symbol
        elif P1_choice == "C2":
            C2 = P_1_symbol
        elif P1_choice == "C3":
            C3 = P_1_symbol
        game_table()

        P2_choice = input("Player 2, choose Your position: ")
        if P2_choice == "A1":
            A1 = P_2_symbol
        elif P2_choice == "A2":
            A2 = P_2_symbol
        elif P2_choice == "A3":
            A3 = P_2_symbol
        elif P2_choice == "B1":
            B1 = P_2_symbol
        elif P2_choice == "B2":
            B2 = P_2_symbol
        elif P2_choice == "B3":
            B3 = P_2_symbol
        elif P2_choice == "C1":
            C1 = P_2_symbol
        elif P2_choice == "C2":
            C2 = P_2_symbol
        elif P2_choice == "C3":
            C3 = P_2_symbol
        game_table()
        game_on = input("Game on? (Y/N): ")

if language == "PL":
    print("Mam nadziej, ze gra sie podobala. Milego dnia!!!")
else:
    print("I hope You've enjoyed the game. Have a nice day!!!")