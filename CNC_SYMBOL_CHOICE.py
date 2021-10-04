def symbol_choice(language):
    right_choice = False

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

    return P_1_symbol , P_2_symbol




