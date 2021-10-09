import re #biblioteka zawierająca między innymi funkcję do znalezienia indesków wszystkich znaków w stringu
import HANGMAN_PENALTY
import getpass  #<- do sprawdzenia

game_on = "t"
while game_on == "t":
    #word = "warszawa"  <- do testowania
    #word = (input("Jakie słowo będzie zgadywane? ")) #jakies tam slowo do testu
    #print("""


























    #""") #póki co, żeby ukryć wybór gracza
    word = getpass.getpass(prompt = "Jakie słowo będzie zgadywane?") #<- działa, ale nie w pycharmie
    word_length = len(word)

    word_hidden = []

    for i in range(0,word_length): #tworzenie listy ukazującej szukane słowo jako ciąg _
        word_hidden.append("_")
    print(f"Szukane słowo składa się z {len(word_hidden)} liter:")
    print(' '.join(word_hidden)) #zamiana listy na string, separatorem między elementami listy jest spacja

    penalty = 0 #zadanie zmiennej penalty
    input_history = [] #otwarcie listy z inputami (co by sie nie powtarzać)

    while penalty < 12:
        taken_symbol = 1
        while taken_symbol == 1: #pętla do sprawdzenia, czy wprowadzana litera, lub słowo się powtórzyło
            symbol = input("Wybierz literę, lub odgadnij całe słowo: ")  # wybieranie literki przez gracza
            inpt_hist_string = ''.join(input_history)
            if inpt_hist_string.find(symbol) >= 0:
                taken_symbol = 1
                print("Litera , lub słowo zostało już wybrane!")

            else:
                taken_symbol = 0
                input_history.append(symbol)

        symbol_index = [_.start() for _ in re.finditer(symbol, word)]  # znalezienie WSZYSTKICH znaków w stringu
        # print(symbol_index)
        # print(len(symbol_index))

        if symbol == word: #sprawdzenie czy odgadnięto słowo
            print(f"Tak, to {word}, WYGRAŁEŚ/ WYGRAŁAŚ!!!")
            break
        elif symbol != word: #wypadek jak literka/ słowo nie zostają odgadnięte
            if len(symbol_index) == 0:
                penalty += 1
                HANGMAN_PENALTY.hangman_penalty(penalty)
            else: #literka odgadnięta
                inserted_value = ""
                for i in range(0, len(symbol_index)):  # wstawianie wybranej literki do listy
                    inserted_value = symbol_index[i]
                    word_hidden[inserted_value] = word[inserted_value]
                print(' '.join(word_hidden))


        if (''.join(word_hidden)) == word:
            print(f"Tak, to {word}, WYGRAŁEŚ/ WYGRAŁAŚ!!!")
            break

    if penalty == 12:
        print(f"Szukanym słowem było: {word}")

    game_on = input("Gramy dalej?(t/n) ")
print("Mam nadzieję, ze gra się podobała. Miłego dnia!!!")

