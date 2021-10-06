class game_core():
    def __init__(self, language, P_1_symbol,P_2_symbol):
        self.language = language
        self.P_1_symbol = P_1_symbol
        self.P_2_symbol = P_2_symbol
        self.P1_choice = " "
        self.P2_choice = " "
        self.game_over = False

    def free_spot_check(self):
        free_spot = False  # Flaga dla pętli sprawdzającej, czy lokacja jest zajęta
        while free_spot != True:  # Pętla sprawdząjąca, czy lokacja jest zajęta
            P1_raw_choice = input(f"Graczu nr 1 ({self.P_1_symbol}), wybierz pozycje: ")
            if P1_raw_choice == "A1" and A1 == " ":
                self.P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "A2" and A2 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "A3" and A3 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "B1" and B1 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "B2" and B2 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "B3" and B3 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "C1" and C1 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "C2" and C2 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            elif P1_raw_choice == "C3" and C3 == " ":
                P1_choice = P1_raw_choice
                free_spot = True
            else:
                print("Zajęte!!/ Zły symbol!!")
                free_spot = False