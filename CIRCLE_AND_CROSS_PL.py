import GAME_LANGUAGE_CHOICE #import pliku z wyborem języka
import CNC_SYMBOL_CHOICE #import pliku z wyborem symbolu

#language = GAME_LANGUAGE_CHOICE.choose_language("KOLKO VS KRZYZYK", "CROSS VS CIRCLE") #wybór języka, zwrot zmiennej language

def CAC_game():

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

    symbol_choice = CNC_SYMBOL_CHOICE.symbol_choice()
    P_1_symbol = symbol_choice[0]
    P_2_symbol = symbol_choice[1]

    game_table()
    print(" ")
    print("Pozycję wybiera się na zasadzie wpsółrzędnych:")
    print(" - Najpierw podajemy współrzędną literkową (A, B, lub C)")
    print(" - Następnie współrzędną cyfrową (1, 2, lub 3)")
    print("Przykład: pozycja A1 oznacza lewy górny róg planszy")
    print(" ")


    #poniżej moduł gry rozbity na 2 języki
    #if language == "PL": #moduł gry dla PL
    P1_choice = " "
    P2_choice = " "
    game_over = False
    while game_over != True:
        free_spot = False #Flaga dla pętli sprawdzającej, czy lokacja jest zajęta
        while free_spot != True: #Pętla sprawdząjąca, czy lokacja jest zajęta
            P1_raw_choice = input(f"Graczu nr 1 ({P_1_symbol}), wybierz pozycje: ").upper()
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
                print("")
                print("Zajęte!!/ Zły symbol!!")
                print("")
                free_spot = False

            print("")


    #poniżej moduł przypisujący lokalizację
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
        print("")
        game_table()
        print("")

    #poniżej moduł sprawdzający warunki wygranej
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
            P2_raw_choice = input(f"Graczu nr 2 ({P_2_symbol}), wybierz pozycje: ").upper()
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
                print("")
                print("Zajęte!!/ Zły symbol!!")
                print("")
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

# else:
#     P1_choice = " "
#     P2_choice = " "
#     game_over = False
#     while game_over != True:
#         free_spot = False  # Flaga dla pętli sprawdzającej, czy lokacja jest zajęta
#         while free_spot != True:  # Pętla sprawdząjąca, czy lokacja jest zajęta
#             P1_raw_choice = input(f"Player 1 ({P_1_symbol}), choose Your location: ")
#             if P1_raw_choice == "A1" and A1 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "A2" and A2 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "A3" and A3 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "B1" and B1 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "B2" and B2 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "B3" and B3 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "C1" and C1 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "C2" and C2 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             elif P1_raw_choice == "C3" and C3 == " ":
#                 P1_choice = P1_raw_choice
#                 free_spot = True
#             else:
#                 print("Taken!!/ Invalid input!!")
#                 free_spot = False
#
#         # poniżej moduł przypisujący lokalizację
#         if P1_choice == "A1":
#             A1 = P_1_symbol
#         elif P1_choice == "A2":
#             A2 = P_1_symbol
#         elif P1_choice == "A3":
#             A3 = P_1_symbol
#         elif P1_choice == "B1":
#             B1 = P_1_symbol
#         elif P1_choice == "B2":
#             B2 = P_1_symbol
#         elif P1_choice == "B3":
#             B3 = P_1_symbol
#         elif P1_choice == "C1":
#             C1 = P_1_symbol
#         elif P1_choice == "C2":
#             C2 = P_1_symbol
#         elif P1_choice == "C3":
#             C3 = P_1_symbol
#         game_table()
#
#         # poniżej moduł sprawdzający warunki wygranej
#         if A1 == P_1_symbol and A2 == P_1_symbol and A3 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif B1 == P_1_symbol and B2 == P_1_symbol and B3 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif C1 == P_1_symbol and C2 == P_1_symbol and C3 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif A1 == P_1_symbol and B1 == P_1_symbol and C1 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif A2 == P_1_symbol and B2 == P_1_symbol and C2 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif A3 == P_1_symbol and B3 == P_1_symbol and C3 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif A1 == P_1_symbol and B2 == P_1_symbol and C3 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif A3 == P_1_symbol and B2 == P_1_symbol and C1 == P_1_symbol:
#             game_over = True
#             print("Player 1 wins!!!")
#         elif A1 != " " and A2 != " " and A3 != " " and B1 != " " and B2 != " " and B3 != " " and C1 != " " and C2 != " " and C3 != " ":
#             game_over = True
#             print("Remis...")
#         else:
#             game_over = False
#
#         if game_over == True:
#             break
#         else:
#             game_over
#
#         free_spot = False  # Flaga dla pętli sprawdzającej, czy lokacja jest zajęta
#         while free_spot != True:  # Pętla sprawdząjąca, czy lokacja jest zajęta
#             P2_raw_choice = input(f"Player 2 ({P_2_symbol}), choose Your location: ")
#             if P2_raw_choice == "A1" and A1 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "A2" and A2 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "A3" and A3 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "B1" and B1 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "B2" and B2 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "B3" and B3 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "C1" and C1 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "C2" and C2 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             elif P2_raw_choice == "C3" and C3 == " ":
#                 P2_choice = P2_raw_choice
#                 free_spot = True
#             else:
#                 print("Taken!!/ Invalid input!!")
#                 free_spot = False
#
#         if P2_choice == "A1":
#             A1 = P_2_symbol
#         elif P2_choice == "A2":
#             A2 = P_2_symbol
#         elif P2_choice == "A3":
#             A3 = P_2_symbol
#         elif P2_choice == "B1":
#             B1 = P_2_symbol
#         elif P2_choice == "B2":
#             B2 = P_2_symbol
#         elif P2_choice == "B3":
#             B3 = P_2_symbol
#         elif P2_choice == "C1":
#             C1 = P_2_symbol
#         elif P2_choice == "C2":
#             C2 = P_2_symbol
#         elif P2_choice == "C3":
#             C3 = P_2_symbol
#         game_table()
#         game_over = False
#
#         if A1 == P_2_symbol and A2 == P_2_symbol and A3 == P_2_symbol:
#             game_over = True
#             print("Player 2 wins!!!")
#         elif B1 == P_2_symbol and B2 == P_2_symbol and B3 == P_2_symbol:
#             game_over = True
#             print("Player 2 wins!!!")
#         elif C1 == P_2_symbol and C2 == P_2_symbol and C3 == P_2_symbol:
#             game_over = True
#             print("Player 2 wins!!!")
#         elif A1 == P_2_symbol and B1 == P_2_symbol and C1 == P_2_symbol:
#             game_over = True
#             print("Player 2 wins!!!")
#         elif A2 == P_2_symbol and B2 == P_2_symbol and C2 == P_2_symbol:
#             game_over = True
#             print("Player 2 wins!!!")
#         elif A3 == P_2_symbol and B3 == P_2_symbol and C3 == P_2_symbol:
#             game_over = True
#             print("Player 2 wins!!!")
#         elif A1 == P_2_symbol and B2 == P_2_symbol and C3 == P_2_symbol:
#             game_over = True
#             print("Player 2 wins!!!")
#         # elif A3 == P_2_symbol and B2 == P_2_symbol and C1 == P_2_symbol:
#         #     game_over = True
#         #     print("Player 2 wins!!!")
#         # elif A1 != " " and A2 != " " and A3 != " " and B1 != " " and B2 != " " and B3 != " " and C1 != " " and C2 != " " and C3 != " ":
#         #     game_over = True
#         #     print("Remis...")
#         # else:
#         #     game_over = False

