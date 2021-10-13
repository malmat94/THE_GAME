print("Witamy w aplikacji THE GAME")
print("")
game_on = "t"

while game_on == "t":
    print("""Wybierz grę w którą chcesz zagrać:
     1. Kołko i krzyżyk (wpisz 1)
     2. Kamień papier nożycę (wpisz 2)
     3. Wisielec (wpisz 3)""")

    print("")

    game = input()

    print("")

    if game == "1": #kółko i krzyżyk
        game_on_1 = "t"
        while game_on_1 == "t":
            import CIRCLE_AND_CROSS_PL

            game_on_1 = input("Gramy dalej w kółko i krzyżyk?(t-tak/n-nie): ").casefold()
            print("")

    elif game == "2": #kamień papier noożyce
        game_on_2 = "t"
        while game_on_2 == "t":
            prs_choice =""
            prs_choice = input("Wybierz tryb gry: pojedynczy gracz(s)/ dwóch graczy(m): ").casefold()
            if prs_choice == "s":
                #from HANGMAN import HANGMAN_PL_SP
                import PAPER_VS_ROCK_VS_SCISSORS_PL_SP

            elif prs_choice == "m":
                #from HANGMAN import HANGMAN_PL_MP
                import PAPER_VS_ROCK_VS_SCISSORS_PL_MP
            print("")

            game_on_2 = input("Gramy dalej w kamień, papier, nożyce?(t-tak/n-nie): ").casefold()
            print("")

    elif game == "3":
        game_on_3 = "t"
        while game_on_3 == "t":
            hang_choice =""
            hang_choice = input("Wybierz tryb gry: pojedynczy gracz(s)/ dwóch graczy(m): ").casefold()
            print(hang_choice)
            if hang_choice == "s":
                #from HANGMAN import HANGMAN_PL_SP
                import HANGMAN_PL_SP

            elif hang_choice == "m":
                #from HANGMAN import HANGMAN_PL_MP
                import HANGMAN_PL_MP
            print("")

            game_on_3 = input("Gramy dalej w wisielca?(t-tak/n-nie): ").casefold()
            print("")

    game_on = input("Chcesz wybrać nową grę?(t-tak/n-nie): ").casefold()
    print("")

print("")
print("Mam nadziej, ze gra sie podobala. Milego dnia!!!")
coles_program = input("Wciśniej ENTER żeby zamknąć grę")