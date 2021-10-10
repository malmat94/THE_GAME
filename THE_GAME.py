print("Witamy w aplikacji THE GAME")
print("""Wybierz grę w którą chcesz zagrać:
 1. Kołko i krzyżyk (wpisz 1)
 2. Kamień papier nożycę (wpisz 2)
 3. Wisielec (wpisz 3)""")

game = input()

if game == "1":
    import CIRCLE_AND_CROSS
elif game == "2":
    import PAPER_VS_ROCK_VS_SCISSORS
elif game == "3":
    import HANGMAN

