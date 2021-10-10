
game_on = "t"

while game_on == "t":
    print("Witamy w aplikacji THE GAME")
    print("""Wybierz grę w którą chcesz zagrać:
     1. Kołko i krzyżyk (wpisz 1)
     2. Kamień papier nożycę (wpisz 2)
     3. Wisielec (wpisz 3)""")

    print("")

    game = input()

    print("")

    if game == "1":
        import CIRCLE_AND_CROSS
    elif game == "2":
        import PAPER_VS_ROCK_VS_SCISSORS
    elif game == "3":
        game_on_3 = "t"
        while game_on_3 == "t":
            hang_choice =""
            hang_choice = input("Wybierz tryb gry: pojedynczy gracz(s)/ dwóch graczy(m): ")
            if hang_choice == "s":
                import HANGMAN_PL_SP

            elif hang_choice == "m":
                import HANGMAN_PL_MP

            game_on_3 = input("Gramy dalej w wisielca?(t-tak/n-nie): ")

    game_on = input("Chcesz wybrać nową grę?(t-tak/n-nie): ")

print("")

coles_program = input("Wciśniej ENTER żeby zamknąć grę")