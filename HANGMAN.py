import re #biblioteka zawierająca między innymi funkcję do znalezienia indesków wszystkich znaków w stringu


word = "asj,fhgbasdlifhoiuasdhfli;asjduhgfoasdf" #jakies tam slowo do testu
word_length = len(word)

word_hidden = []

for i in range(0,word_length): #tworzenie listy ukazującej szukane słowo jako ciąg _
    word_hidden.append("_")

print(word_hidden)

choosen_symbol = "s" #wybrany symbol

word_all_index = [_.start() for _ in re.finditer(choosen_symbol, word)] #znalezienie WSZYSTKICH znaków w stringu

print(len(word_all_index))

inserted_value = ""
for i in range(0, len(word_all_index)): #wstawianie wybranej literki do listy
    inserted_value = word_all_index[i]
    word_hidden[inserted_value] = word[inserted_value]

print(word_hidden)







