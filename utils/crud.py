
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


########okno_przychodnie_crud
def lista_przychodni(listbox_lista_przychodni):
    listbox_lista_przychodni.delete(0, END)
    for idx, przychodnia in enumerate(przychodnie):
        listbox_lista_przychodni.insert(idx,
                                        f'{przychodnia.nazwa}  {przychodnia.doktorzy} {przychodnia.pacjenci} {przychodnia.lokalizacja}')


def dodaj_przychodnie(entry_nazwa, entry_doktorzy, entry_pacjenci, entry_lokalizacja, listbox_lista_przychodni):
    nazwa = entry_nazwa.get()
    doktorzy = entry_doktorzy.get()
    pacjenci = entry_pacjenci.get()
    lokalizacja = entry_lokalizacja.get()
    print(nazwa, doktorzy, pacjenci, lokalizacja)
    przychodnie.append(przychodnia(nazwa, doktorzy, pacjenci, lokalizacja))
    lista_przychodni(listbox_lista_przychodni)

    entry_nazwa.delete(0, END)
    entry_doktorzy.delete(0, END)
    entry_pacjenci.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_nazwa.focus()


def usun_przychodnie(listbox_lista_przychodni):
    i = listbox_lista_przychodni.index(ACTIVE)
    print(i)
    przychodnie.pop(i)
    lista_przychodni(listbox_lista_przychodni)


def pokaz_szczegoly_przychodni(listbox_lista_przychodni, label_nazwa_szczegoly_obiektu_wartosc,
                               label_doktorzy_szczegoly_obiektu_wartosc, label_pacjenci_szczegoly_obiektu_wartosc,
                               label_lokalizacja_szczegoly_obiektu_wartosc):
    i = listbox_lista_przychodni.index(ACTIVE)
    nazwa = przychodnie[i].nazwa
    label_nazwa_szczegoly_obiektu_wartosc.config(text=nazwa)
    doktorzy = przychodnie[i].doktorzy
    label_doktorzy_szczegoly_obiektu_wartosc.config(text=doktorzy)
    pacjenci = przychodnie[i].pacjenci
    label_pacjenci_szczegoly_obiektu_wartosc.config(text=pacjenci)
    lokalizacja = przychodnie[i].lokalizacja
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=lokalizacja)


def edytuj_przychodnie(listbox_lista_przychodni, entry_nazwa, entry_doktorzy, entry_pacjenci, entry_lokalizacja,
                       button_dodaj_przychodnie):
    i = listbox_lista_przychodni.index(ACTIVE)
    entry_nazwa.insert(0, przychodnie[i].nazwa)
    entry_doktorzy.insert(0, przychodnie[i].doktorzy)
    entry_pacjenci.insert(0, przychodnie[i].pacjenci)
    entry_lokalizacja.insert(0, przychodnie[i].lokalizacja)

    button_dodaj_przychodnie.config(text="Zapisz zmiany",
                                    command=lambda: aktualizuj_przychodnie(i, entry_nazwa, entry_doktorzy,
                                                                           entry_pacjenci, entry_lokalizacja,
                                                                           button_dodaj_przychodnie,
                                                                           listbox_lista_przychodni))


def aktualizuj_przychodnie(i, entry_nazwa, entry_doktorzy, entry_pacjenci, entry_lokalizacja, button_dodaj_uzytkownia,
                           listbox_lista_przychodni):
    przychodnie[i].nazwa = entry_nazwa.get()
    przychodnie[i].doktorzy = entry_doktorzy.get()
    przychodnie[i].pacjenci = entry_pacjenci.get()
    przychodnie[i].lokalizacja = entry_lokalizacja.get()
    lista_przychodni(listbox_lista_przychodni)
    button_dodaj_uzytkownia.config(text="Dodaj uzytkownikow", command=dodaj_przychodnie)
    entry_nazwa.delete(0, END)
    entry_doktorzy.delete(0, END)
    entry_pacjenci.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_nazwa.focus()


#####okno przychodnie crud




##### okno lekarze crud
def lista_lekarzy(listbox_lista_lekarzy):
    listbox_lista_lekarzy.delete(0, END)
    for idx, lekarz in enumerate(lekarze):
        listbox_lista_lekarzy.insert(idx,
                                     f'{lekarz.imie}  {lekarz.nazwisko} {lekarz.placowka} {lekarz.przynalezni_pacjenci} {lekarz.pochodzenie}')


def zatrudnij_doktora(entry_imie, entry_nazwisko, entry_placowka, entry_przynalezni_pacjenci, entry_pochodenie,
                      listbox_lista_lekarzy):
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    placowka = entry_placowka.get()
    przynalezni_pacjenci = entry_przynalezni_pacjenci.get()
    pochodzenie = entry_pochodenie.get()
    print(imie, nazwisko, placowka, przynalezni_pacjenci, pochodzenie)
    lekarze.append(lekarz(imie, nazwisko, placowka, przynalezni_pacjenci, pochodzenie))
    lista_lekarzy(listbox_lista_lekarzy)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_placowka.delete(0, END)
    entry_przynalezni_pacjenci.delete(0, END)
    entry_pochodenie.delete(0, END)

    entry_imie.focus()


def zwolnij_doktora(listbox_lista_lekarzy):
    i = listbox_lista_lekarzy.index(ACTIVE)
    print(i)
    lekarze.pop(i)
    lista_lekarzy(listbox_lista_lekarzy)


def informacje_o_doktorze(listbox_lista_lekarzy, label_imie_szczegoly_obiektu_wartosc,
                          label_nazwisko_szczegoly_obiektu_wartosc, label_placowka_szczegoly_obiektu_wartosc,
                          label_przynalezni_pacjenci_szczegoly_obiektu_wartosc,
                          label_pochodzenie_szczegoly_obietu_wartosc):
    i = listbox_lista_lekarzy.index(ACTIVE)
    imie = lekarze[i].imie
    nazwisko = lekarze[i].nazwisko
    placowka = lekarze[i].placowka
    przynalezni_pacjenci = lekarze[i].przynalezni_pacjenci
    pochodzenie = lekarze[i].pochodzenie

    label_imie_szczegoly_obiektu_wartosc.config(text=imie)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
    label_placowka_szczegoly_obiektu_wartosc.config(text=placowka)
    label_przynalezni_pacjenci_szczegoly_obiektu_wartosc.config(text=przynalezni_pacjenci)
    label_pochodzenie_szczegoly_obietu_wartosc.config(text=pochodzenie)


def edytuj_doktora(listbox_lista_lekarzy, entry_imie, entry_nazwisko, entry_placowka, entry_przynalezni_pacjenci,
                   entry_pochodzenie,
                   button_zatrudnij_doktora):
    i = listbox_lista_lekarzy.index(ACTIVE)
    entry_imie.insert(0, lekarze[i].imie)
    entry_nazwisko.insert(0, lekarze[i].nazwisko)
    entry_placowka.insert(0, lekarze[i].placowka)
    entry_przynalezni_pacjenci.insert(0, lekarze[i].przynalezni_pacjenci)
    entry_pochodzenie.insert(0, lekarze[i].pochodzenie)

    button_zatrudnij_doktora.config(text="Zapisz zmiany",
                                    command=lambda: aktualizuj_doktora(i, entry_imie, entry_nazwisko,
                                                                       entry_placowka, entry_przynalezni_pacjenci,
                                                                       entry_pochodzenie,
                                                                       button_zatrudnij_doktora,
                                                                       listbox_lista_lekarzy))


def aktualizuj_doktora(i, entry_imie, entry_nazwisko, entry_placowka, entry_przynalezni_pacjenci, entry_pochodzenie,
                       button_zatrudnij_doktora,
                       listbox_lista_lekarzy):
    lekarze[i].imie = entry_imie.get()
    lekarze[i].nazwisko = entry_nazwisko.get()
    lekarze[i].placowka = entry_placowka.get()
    lekarze[i].przynalezni_pacjenci = entry_przynalezni_pacjenci.get()
    lekarze[i].pochodzenie = entry_pochodzenie.get()
    lista_lekarzy(listbox_lista_lekarzy)
    button_zatrudnij_doktora.config(text="Zaktualizuj dane o doktorze", command=zatrudnij_doktora)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_placowka.delete(0, END)
    entry_przynalezni_pacjenci.delete(0, END)
    entry_pochodzenie.delete(0, END)
    entry_imie.focus()


######okno lekarze crud




#######okno pacjenci crud
def lista_pacjentow(listbox_lista_Pacjentow):
    listbox_lista_Pacjentow.delete(0, END)
    for idx, Pacjent in enumerate(Pacjenci):
        listbox_lista_Pacjentow.insert(idx,
                                        f'{Pacjent.Imie}  {Pacjent.Nazwisko} {Pacjent.Przychodnia} {Pacjent.Lokalizacja}')


def dodaj_pacjenta(entry_Imie, entry_Nazwisko, entry_Przychodnia, entry_Lokalizacja, listbox_lista_Pacjentow):
    Imie = entry_Imie.get()
    Nazwisko = entry_Nazwisko.get()
    Przychodnia = entry_Przychodnia.get()
    Lokalizacja = entry_Lokalizacja.get()
    print(Imie, Nazwisko, Przychodnia, Lokalizacja)
    Pacjenci.append(Pacjent(Imie, Nazwisko, Przychodnia, Lokalizacja))
    lista_pacjentow(listbox_lista_Pacjentow)

    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Przychodnia.delete(0, END)
    entry_Lokalizacja.delete(0, END)

    entry_Imie.focus()


def usun_pacjenta(listbox_lista_Pacjentow):
    i = listbox_lista_Pacjentow.index(ACTIVE)
    print(i)
    Pacjenci.pop(i)
    lista_pacjentow(listbox_lista_Pacjentow)


def pokaz_szczegoly_pacjenta(listbox_lista_Pacjentow, label_Imie_szczegoly_obiektu_wartosc,
                               label_Nazwisko_szczegoly_obiektu_wartosc, label_Przychodnia_szczegoly_obiektu_wartosc,
                               label_Lokalizacja_szczegoly_obiektu_wartosc):
    i = listbox_lista_Pacjentow.index(ACTIVE)
    Imie = Pacjenci[i].Imie
    label_Imie_szczegoly_obiektu_wartosc.config(text=Imie)
    Nazwisko = Pacjenci[i].Nazwisko
    label_Nazwisko_szczegoly_obiektu_wartosc.config(text=Nazwisko)
    Przychodnia = Pacjenci[i].Przychodnia
    label_Przychodnia_szczegoly_obiektu_wartosc.config(text=Przychodnia)
    Lokalizacja = Pacjenci[i].Lokalizacja
    label_Lokalizacja_szczegoly_obiektu_wartosc.config(text=Lokalizacja)


def edytuj_pacjenta(listbox_lista_Pacjentow, entry_Imie, entry_Nazwisko, entry_Przychodnia, entry_Lokalizacja,
                       button_dodaj_pacjenta):
    i = listbox_lista_Pacjentow.index(ACTIVE)
    entry_Imie.insert(0, Pacjenci[i].Imie)
    entry_Nazwisko.insert(0, Pacjenci[i].Nazwisko)
    entry_Przychodnia.insert(0, Pacjenci[i].Przychodnia)
    entry_Lokalizacja.insert(0, Pacjenci[i].Lokalizacja)

    button_dodaj_pacjenta.config(text="Zapisz zmiany",
                                    command=lambda: aktualizuj_pacjenta(i, entry_Imie, entry_Nazwisko,
                                                                           entry_Przychodnia, entry_Lokalizacja,
                                                                           button_dodaj_pacjenta,
                                                                           listbox_lista_Pacjentow))


def aktualizuj_pacjenta(i, entry_Imie, entry_Nazwisko, entry_Przychodnia, entry_Lokalizacja, button_dodaj_pacjenta,
                           listbox_lista_Pacjentow):
    Pacjenci[i].Imie = entry_Imie.get()
    Pacjenci[i].Nazwisko = entry_Nazwisko.get()
    Pacjenci[i].Przychodnia = entry_Przychodnia.get()
    Pacjenci[i].Lokalizacja = entry_Lokalizacja.get()
    lista_pacjentow(listbox_lista_Pacjentow)
    button_dodaj_pacjenta.config(text="Dodaj pacjenta", command=dodaj_pacjenta)
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Przychodnia.delete(0, END)
    entry_Lokalizacja.delete(0, END)
    entry_Imie.focus()

######okno pacjenci crud