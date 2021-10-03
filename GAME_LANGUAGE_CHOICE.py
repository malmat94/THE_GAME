def choose_language(nazwa_gry, games_name):
    language_choice = False
    while language_choice != True:

        language = input("Wybierz jezyk/ Choose Your language(PL/ENG): ")
        print(" ")

        if language == "PL":
            language_respond = "Witamy w grze "
            language_choice = True
            print(f"{language_respond}{nazwa_gry}!!!")
        elif language == "ENG":
            language_respond = "Welcome to the "
            language_choice = True
            print(f"{language_respond}{games_name} game!!!")
        else:
            language_respond = "Niewlasciwy wybor, sporbuj ponownie/ Invalid choice, try again!"
            language_choice = False
            print(language_respond)
    return language