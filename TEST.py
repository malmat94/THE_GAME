taken_symbol = 1
input_history = ['a']
while taken_symbol == 1:
    symbol = input("Wybierz literę, lub odgadnij całe słowo: ")  # wybieranie literki przez gracza
    inpt_hist_string =''.join(input_history)
    if inpt_hist_string.find(symbol) >= 0:
        taken_symbol = 1
        print("Litera , lub słowo zostało już wybrane!")

    else:
        taken_symbol = 0
        input_history.append(symbol)