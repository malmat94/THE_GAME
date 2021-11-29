import re #biblioteka zawierająca między innymi funkcję do znalezienia indesków wszystkich znaków w stringu
import HANGMAN_PENALTY
import getpass  #<- DZIAŁA, ALE NIE W PYCHARMIE
import random

def HANGMAN_SP_GAME():
    easy_words_list = ["kot", "pies", "bąk", "mysz", "auto", "ser", "chleb", "stół", "koc", "kupa", "krew", "ptak", "trup", "pręt", "próg", "tran", "kara", "para", "ucho", "oko"]
    medium_words_list = ["pręgi", "książka", "samochód", "trzcina", "klamka", "dupsko", "szuflada", "python", "koparka", "słonina", "sarna", "papuga", "kotlet", "kominek", "lewarek", "ogródek", "łóżko"]
    hard_words_list = ["karmazyn", "grzegrzółka", "szczęście", "ambiwalętny", "koncelebra", "tabernakulum", "eskalacja", "degeneracja", "emancypacja", "przedsiębierna", "konfabulacja"]
    deadly_words_list = ["konstantynopolitańczykowianeczka", "pięćdziesięciogroszówka", "europarlamentarzysta", "niepodległościowiec", "dźwiękonaśladownictwo", "antropomorfizacja", "lumpenproletariat"]

    print("""Wybierz poziom trudności:
        1. łatwy
        2. średni
        3. trudny
        4. zabójczy""")

    dif_level = int(input())

    if dif_level == 1:
        random_index = random.randrange(0, len(easy_words_list))
        word = easy_words_list[random_index]
    elif dif_level == 2:
        random_index = random.randrange(0, len(medium_words_list))
        word = medium_words_list[random_index]
    elif dif_level == 3:
        random_index = random.randrange(0, len(hard_words_list))
        word = hard_words_list[random_index]
    elif dif_level == 4:
        random_index = random.randrange(0, len(deadly_words_list))
        word = deadly_words_list[random_index]

    word_length = len(word)

    word_hidden = []

    for i in range(0,word_length): #tworzenie listy ukazującej szukane słowo jako ciąg _
        word_hidden.append("_")
    print(f"Szukane słowo składa się z {len(word_hidden)} liter:")
    print(' '.join(word_hidden)) #zamiana listy na string, separatorem między elementami listy jest spacja

    penalty = 0 #zadanie zmiennej penalty
    input_history = [] #otwarcie listy z inputami (co by sie nie powtarzać)

    while penalty < 12:
        print("")
        taken_symbol = 1
        while taken_symbol == 1: #pętla do sprawdzenia, czy wprowadzana litera, lub słowo się powtórzyło
            symbol = input("Wybierz literę, lub odgadnij całe słowo: ").casefold()  # wybieranie literki przez gracza
            print("")
            if input_history.count(symbol) > 0:
                taken_symbol = 1
                print("Litera , lub słowo zostało już wybrane!")

            else:
                taken_symbol = 0
                input_history.append(symbol)

        symbol_index = [_.start() for _ in re.finditer(symbol, word)]  # znalezienie WSZYSTKICH znaków w stringu
        #print(symbol_index)
        #print(len(symbol_index))

        if symbol == word: #sprawdzenie czy odgadnięto słowo
            print(f"Tak, to {word}, WYGRAŁEŚ/ WYGRAŁAŚ!!!")
            break
        elif symbol != word: #przypadek gdy słowno nie zostało do razu odgadnięte
            if len(symbol) == 1: #sprawdzenie czy wybrana literka się zgadza

                if len(symbol_index) == 0: #jeżeli się nie zgadza
                    penalty += 1
                    HANGMAN_PENALTY.hangman_penalty(penalty)
                    print(' '.join(word_hidden))

                else: #jeżeli się zgadza
                    inserted_value = ""
                    for i in range(0, len(symbol_index)):  # wstawianie wybranej literki do listy
                        inserted_value = symbol_index[i]
                        word_hidden[inserted_value] = word[inserted_value]
                    print(' '.join(word_hidden))
            else: #jeżeli wpisano ciągn znaków nie zgadzający się z odgadywanym słowem
                penalty += 1
                HANGMAN_PENALTY.hangman_penalty(penalty)
                print(' '.join(word_hidden))


        if (''.join(word_hidden)) == word:
            print(f"Tak, to {word}, WYGRAŁEŚ/ WYGRAŁAŚ!!!")
            break

        if penalty == 12:
            print(f"Szukanym słowem było: {word}")



