def hangman_penalty(penalty):

    try_1 = """






/"""

    try_2 = """






/ \ """

    try_3 = """
 |
 |
 |
 |
 | 
 |
/|\ """

    try_4 = """
 |/
 |
 |
 |
 | 
 |
/|\ """

    try_5 = """__________
 |/
 |
 |
 |
 | 
 |
/|\ """

    try_6 = """__________
 |/     |
 |      |
 |
 |
 | 
 |
/|\ """

    try_7 = """__________
 |/     |
 |      |
 |      O
 |
 | 
 |
/|\ """

    try_8 = """__________
 |/     |
 |      |
 |      O
 |     /
 | 
 |
/|\ """

    try_9 = """__________
 |/     |
 |      |
 |      O
 |     /|
 | 
 |
/|\ """

    try_10 = """__________
 |/     |
 |      |
 |      O
 |     /|\ 
 | 
 |
/|\ """

    try_11 = """__________
 |/     |
 |      |
 |      O
 |     /|\ 
 |     /
 |
/|\ """

    try_12 = """__________
 |/     |
 |      |
 |      O
 |     /|\ 
 |     / \ 
 |
/|\ """

    if penalty == '1':
        print(try_1)
    elif penalty == '2':
        print(try_2)
    elif penalty == '3':
        print(try_3)
    elif penalty == '4':
        print(try_4)
    elif penalty == '5':
        print(try_5)
    elif penalty == '6':
        print(try_6)
    elif penalty == '7':
        print(try_7)
    elif penalty == '8':
        print(try_8)
    elif penalty == '9':
        print(try_9)
    elif penalty == '10':
        print(try_10)
    elif penalty == '11':
        print(try_11)
    elif penalty == '12':
        print(try_12)


#test, odkomentuj
#penalty_input = input("Ile w dupe? ")

#hangman_penalty(penalty_input)
