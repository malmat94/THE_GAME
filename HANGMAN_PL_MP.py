import re #biblioteka zawierająca między innymi funkcję do znalezienia indesków wszystkich znaków w stringu
import HANGMAN_PENALTY
import getpass  #<- do sprawdzenia

def HANGMAN_MP_GAME():
    #word = "warszawa"  <- do testowania
    #word = (input("Jakie słowo będzie zgadywane? ")) #jakies tam slowo do testu

    word = getpass.getpass(prompt = "Jakie słowo będzie zgadywane?").casefold() #<- działa, ale nie w pycharmie
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



