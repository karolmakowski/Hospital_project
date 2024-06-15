
#######logowanie
login_1: str = ""
login_2: str = ""
login_3: str = ""
login_4: str = ""
login_5: str = ""
login_6: str = ""
login_7: str = ""
login_8: str = ""
login_9: str = ""
login_10: str = "w"
haslo_1: str = ""
haslo_2: str = ""
haslo_3: str = ""
haslo_4: str = ""
haslo_5: str = ""
haslo_6: str = ""
haslo_7: str = ""
haslo_8: str = ""
haslo_9: str = ""
haslo_10: str = "w"


def logowanie():
    while True:
        login = input("Podaj login: ")
        haslo = input("Wpisz: ")

        if (login == login_1 and haslo == haslo_1) or \
                (login == login_2 and haslo == haslo_2) or \
                (login == login_3 and haslo == haslo_3) or \
                (login == login_4 and haslo == haslo_4) or \
                (login == login_5 and haslo == haslo_5) or \
                (login == login_6 and haslo == haslo_6) or \
                (login == login_7 and haslo == haslo_7) or \
                (login == login_8 and haslo == haslo_8) or \
                (login == login_9 and haslo == haslo_9) or \
                (login == login_10 and haslo == haslo_10):
            print("Dostęp przyznany")
            break
        else:
            print("Błędne dane logowania. Spróbuj ponownie.")


logowanie()
#######logowanie
