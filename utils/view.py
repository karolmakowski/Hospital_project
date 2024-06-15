from tkinter import *
from models import data_source


class przychodnia:
    def __init__(self, nazwa, doktorzy, pacjenci, lokalizacja):
        self.nazwa = nazwa
        self.doktorzy = doktorzy
        self.pacjenci = pacjenci
        self.lokalizacja = lokalizacja


login_1: str = "ARafał"
login_2: str = "RAndrzej"
login_3: str = "MArtur"
login_4: str = "AMichał"
login_5: str = "KMarcin"
login_6: str = "MKarol"
login_7: str = "JMagda"
login_8: str = "MJoanna"
login_9: str = "OPaulina"
login_10: str = "POliwia"
haslo_1: str = "Medica1"
haslo_2: str = "Medica2"
haslo_3: str = "Care1"
haslo_4: str = "Care2"
haslo_5: str = "Lux1"
haslo_6: str = "Lux2"
haslo_7: str = "Marvit1"
haslo_8: str = "Marvit2"
haslo_9: str = "Prima1"
haslo_10: str = "Prima2"

przychodnie = []


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


def okno_przychodnie(root):
    przychodnie_root = Toplevel(root)
    przychodnie_root.title("Lista przychodni")
    przychodnie_root.geometry("1024x720")


    # ramki do porządkowania struktury
    ramka_lista_przychodni = Frame(przychodnie_root)
    ramka_formularz = Frame(przychodnie_root)
    ramka_szczegoly_obiektu = Frame(przychodnie_root)

    ramka_lista_przychodni.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista_placowek
    label_lista_przychodni = Label(ramka_lista_przychodni, text="Lista przychodni: ")
    listbox_lista_przychodni = Listbox(ramka_lista_przychodni, width=50)
    button_pokaz_szczegoly = Button(ramka_lista_przychodni, text="Pokaż szczegóły",
                                    command=lambda: pokaz_szczegoly_przychodni(listbox_lista_przychodni,
                                                                               label_nazwa_szczegoly_obiektu_wartosc,
                                                                               label_doktorzy_szczegoly_obiektu_wartosc,
                                                                               label_pacjenci_szczegoly_obiektu_wartosc,
                                                                               label_lokalizacja_szczegoly_obiektu_wartosc))
    button_usun_obiekt = Button(ramka_lista_przychodni, text='Usuń obiekt',
                                command=lambda: usun_przychodnie(listbox_lista_przychodni))
    button_edytuj_obiektu = Button(ramka_lista_przychodni, text='Edytuj obiekt',
                                   command=lambda: edytuj_przychodnie(listbox_lista_przychodni, entry_nazwa,
                                                                      entry_doktorzy, entry_pacjenci,
                                                                      entry_lokalizacja, button_dodaj_przychodnie))

    label_lista_przychodni.grid(row=0, column=0, columnspan=3)
    listbox_lista_przychodni.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly.grid(row=2, column=0)
    button_usun_obiekt.grid(row=2, column=1)
    button_edytuj_obiektu.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Formularz")
    label_nazwa = Label(ramka_formularz, text="Nazwa: ")
    label_doktorzy = Label(ramka_formularz, text="Doktorzy: ")
    label_pacjenci = Label(ramka_formularz, text="Pacjenci: ")
    label_lokalizacja = Label(ramka_formularz, text="Lokalizacja")

    entry_nazwa = Entry(ramka_formularz)
    entry_doktorzy = Entry(ramka_formularz)
    entry_pacjenci = Entry(ramka_formularz)
    entry_lokalizacja = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_nazwa.grid(row=1, column=0, sticky=W)
    label_doktorzy.grid(row=2, column=0, sticky=W)
    label_pacjenci.grid(row=3, column=0, sticky=W)
    label_lokalizacja.grid(row=4, column=0, sticky=W)

    entry_nazwa.grid(row=1, column=1)
    entry_doktorzy.grid(row=2, column=1)
    entry_pacjenci.grid(row=3, column=1)
    entry_lokalizacja.grid(row=4, column=1)

    button_dodaj_przychodnie = Button(ramka_formularz, text="Dodaj przychodnię",
                                      command=lambda: dodaj_przychodnie(entry_nazwa, entry_doktorzy, entry_pacjenci,
                                                                        entry_lokalizacja, listbox_lista_przychodni))
    button_dodaj_przychodnie.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu

    label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły przychodni: ")
    label_nazwa_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwa: ")
    label_doktorzy_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Doktorzy: ")
    label_pacjenci_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Pacjenci: ")
    label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja: ")

    label_nazwa_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_doktorzy_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_pacjenci_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
    label_nazwa_szczegoly_obiektu.grid(row=1, column=0,)
    label_nazwa_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_doktorzy_szczegoly_obiektu.grid(row=1, column=2)
    label_doktorzy_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    label_pacjenci_szczegoly_obiektu.grid(row=1, column=4)
    label_pacjenci_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
    label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)




class lekarz:
    def __init__(self, imie, nazwisko, placowka, przynalezni_pacjenci, pochodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.placowka = placowka
        self.przynalezni_pacjenci = przynalezni_pacjenci
        self.pochodzenie = pochodzenie

lekarze = []
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


def okno_lekarze(root):
    lekarze_root = Toplevel(root)
    lekarze_root.title("Lista przychodni")
    lekarze_root.geometry("1024x720")

    # ramki do porządkowania struktury
    ramka_lista_lekarzy = Frame(lekarze_root)
    ramka_formularz = Frame(lekarze_root)
    ramka_informacje_o_doktorze = Frame(lekarze_root)

    ramka_lista_lekarzy.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_informacje_o_doktorze.grid(row=1, column=0, columnspan=2)

    # lista_lekarzy
    label_lista_lekarzy = Label(ramka_lista_lekarzy, text="Lista lekarzy: ")
    listbox_lista_lekarzy = Listbox(ramka_lista_lekarzy, width=80)
    button_pokaz_szczegoly = Button(ramka_lista_lekarzy, text="Pokaż szczegóły",
                                    command=lambda: informacje_o_doktorze(listbox_lista_lekarzy,
                                                                          label_imie_szczegoly_obiektu_wartosc,
                                                                          label_nazwisko_szczegoly_obiektu_wartosc,
                                                                          label_placowka_szczegoly_obiektu_wartosc,
                                                                          label_przynalezni_pacjenci_szczegoly_obiektu_wartosc,
                                                                          label_pochodzenie_szczegoly_obiektu_wartosc))
    button_zwolnij_doktora = Button(ramka_lista_lekarzy, text='Zwolnij doktora',
                                    command=lambda: zwolnij_doktora(listbox_lista_lekarzy))
    button_edytuj_dane = Button(ramka_lista_lekarzy, text='Edytuj informacje o doktorze',
                                command=lambda: edytuj_doktora(listbox_lista_lekarzy, entry_imie,
                                                               entry_nazwisko, entry_placowka,
                                                               entry_przynalezni_pacjenci, entry_pochodzenie,
                                                               button_zatrudnij_doktora))

    label_lista_lekarzy.grid(row=0, column=0, columnspan=3)
    listbox_lista_lekarzy.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly.grid(row=2, column=0)
    button_zwolnij_doktora.grid(row=2, column=1)
    button_edytuj_dane.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Formularz")
    label_imie = Label(ramka_formularz, text="Imię: ")
    label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
    label_placowka = Label(ramka_formularz, text="Placówka: ")
    label_przynalezni_pacjenci = Label(ramka_formularz, text="Przynależni pacjenci: ")
    label_pochodzenie = Label(ramka_formularz, text="Pochodzenie: ")

    entry_imie = Entry(ramka_formularz)
    entry_nazwisko = Entry(ramka_formularz)
    entry_placowka = Entry(ramka_formularz)
    entry_przynalezni_pacjenci = Entry(ramka_formularz)
    entry_pochodzenie = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_imie.grid(row=1, column=0, sticky=W)
    label_nazwisko.grid(row=2, column=0, sticky=W)
    label_placowka.grid(row=3, column=0, sticky=W)
    label_przynalezni_pacjenci.grid(row=4, column=0, sticky=W)
    label_pochodzenie.grid(row=5, column=0, sticky=W)

    entry_imie.grid(row=1, column=1)
    entry_nazwisko.grid(row=2, column=1)
    entry_placowka.grid(row=3, column=1)
    entry_przynalezni_pacjenci.grid(row=4, column=1)
    entry_pochodzenie.grid(row=5, column=1)

    button_zatrudnij_doktora = Button(ramka_formularz, text="Zatrudnij doktora",
                                      command=lambda: zatrudnij_doktora(entry_imie, entry_nazwisko, entry_placowka,
                                                                        entry_przynalezni_pacjenci, entry_pochodzenie,
                                                                        listbox_lista_lekarzy))
    button_zatrudnij_doktora.grid(row=6, column=1, columnspan=2)

    # szczegoly obiektu

    label_szczegoly_obiektu = Label(ramka_informacje_o_doktorze, text="Informacje o doktorze: ")
    label_imie_szczegoly_obiektu = Label(ramka_informacje_o_doktorze, text="Imię: ")
    label_nazwisko_szczegoly_obiektu = Label(ramka_informacje_o_doktorze, text="Nazwisko: ")
    lebel_placowka_szczegoly_obiektu = Label(ramka_informacje_o_doktorze, text="Placówka: ")
    label_przynalezni_pacjenci_szczegoly_obiektu = Label(ramka_informacje_o_doktorze, text="Przynależni pacjenci: ")
    label_pochodzenie_szczegoly_obiektu = Label(ramka_informacje_o_doktorze, text="Pochodzenie: ")

    label_imie_szczegoly_obiektu_wartosc = Label(ramka_informacje_o_doktorze, text="...")
    label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_informacje_o_doktorze, text="...")
    label_placowka_szczegoly_obiektu_wartosc = Label(ramka_informacje_o_doktorze, text="...")
    label_przynalezni_pacjenci_szczegoly_obiektu_wartosc = Label(ramka_informacje_o_doktorze, text="...")
    label_pochodzenie_szczegoly_obiektu_wartosc = Label(ramka_informacje_o_doktorze, text="...")

    label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
    label_imie_szczegoly_obiektu.grid(row=1, column=0)
    label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
    label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    lebel_placowka_szczegoly_obiektu.grid(row=1, column=4)
    label_placowka_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_przynalezni_pacjenci_szczegoly_obiektu.grid(row=1, column=6)
    label_przynalezni_pacjenci_szczegoly_obiektu_wartosc.grid(row=1, column=7)
    label_pochodzenie_szczegoly_obiektu.grid(row=1, column=8)
    label_pochodzenie_szczegoly_obiektu_wartosc.grid(row=1, column=9)

def logowanie():
    while True:
        login = input("Podaj login: ")
        haslo = input("Wpisz hasło: ")

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
            root = Tk()
            root.title("Przychodnie w pobliżu")
            root.geometry("800x500")

            label = Label(root, text="Wybierz opcję:")
            label.grid(row=0, column=0, columnspan=3)

            button1 = Button(root, text="Lista przychodni",
                             command=lambda: okno_przychodnie(root))
            button1.grid(row=1, column=0)

            button2 = Button(root, text="Lista lekarzy",
                             command=lambda: okno_lekarze(root))
            button2.grid(row=1, column=1)

            button3 = Button(root, text="Lista pacjentów",
                             command=lambda: okno_przychodnie(root))
            button3.grid(row=1, column=2)

            root.mainloop()
            break
        else:
            print("Błędne dane logowania. Spróbuj ponownie.")


logowanie()
