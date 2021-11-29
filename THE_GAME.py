from PAPER_VS_ROCK_VS_SCISSORS_PL_SP import PRS_Single_game
from PAPER_VS_ROCK_VS_SCISSORS_PL_MP import PRS_Multi_game
from CIRCLE_AND_CROSS_PL import CAC_game
from HANGMAN_PL_MP import HANGMAN_MP_GAME
from HANGMAN_PL_SP import HANGMAN_SP_GAME

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
            CAC_game()

            game_on_1 = input("Gramy dalej w kółko i krzyżyk?(t-tak/n-nie): ").casefold()
            while True:

                if game_on_1 == "t" or game_on_1 == "n":
                    break
                else:
                    print("Zły znak!!")
                    print("")
                    game_on_1 = input("Gramy dalej w kółko i krzyżyk?(t-tak/n-nie): ").casefold()
            print("")

    elif game == "2": #kamień papier noożyce
        game_on_2 = "t"
        while game_on_2 == "t":
            prs_choice =""
            prs_choice = input("Wybierz tryb gry: pojedynczy gracz(s)/ dwóch graczy(m): ").casefold()
            while True:

                if prs_choice == "s" or prs_choice == "m":
                    break
                else:
                    print("Zły znak!!")
                    print("")
                    prs_choice = input("Wybierz tryb gry: pojedynczy gracz(s)/ dwóch graczy(m): ").casefold()

            if prs_choice == "s":
                #from HANGMAN import HANGMAN_PL_SP
                print("")
                PRS_Single_game()

            elif prs_choice == "m":
                #from HANGMAN import HANGMAN_PL_MP
                print("")
                PRS_Multi_game()
            print("")

            game_on_2 = input("Gramy dalej w kamień, papier, nożyce?(t-tak/n-nie): ").casefold()
            while True:

                if game_on_2 == "t" or game_on_2 == "n":
                    break
                else:
                    print("Zły znak!!")
                    print("")
                    game_on_2 = input("Gramy dalej w kamień, papier, nożyce?(t-tak/n-nie): ").casefold()
            print("")

    elif game == "3":
        game_on_3 = "t"
        while game_on_3 == "t":
            hang_choice: str =""
            hang_choice = input("Wybierz tryb gry: pojedynczy gracz(s)/ dwóch graczy(m): ").casefold()
            while True:

                if hang_choice == "s" or hang_choice == "m":
                    break
                else:
                    print("Zły znak!!")
                    print("")
                    hang_choice = input("Wybierz tryb gry: pojedynczy gracz(s)/ dwóch graczy(m): ").casefold()

            if hang_choice == "s":
                HANGMAN_SP_GAME()

            elif hang_choice == "m":
                HANGMAN_MP_GAME()

            print("")

            game_on_3 = input("Gramy dalej w wisielca?(t-tak/n-nie): ").casefold()
            while True:

                if game_on_3 == "t" or game_on_3 == "n":
                    break
                else:
                    print("Zły znak!!")
                    print("")
                    game_on_3 = input("Gramy dalej w wisielca?(t-tak/n-nie): ").casefold()
            print("")

    game_on = input("Chcesz wybrać nową grę?(t-tak/n-nie): ").casefold()
    while True:

        if game_on == "t" or game_on == "n":
            break
        else:
            print("Zły znak!!")
            print("")
            game_on = input("Chcesz wybrać nową grę?(t-tak/n-nie): ").casefold()
    print("")

print("")
print("Mam nadzieję, że gra się podobała. Miłego dnia!!!")
coles_program = input("Wciśniej ENTER żeby zamknąć grę")