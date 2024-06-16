from tkinter import *
import requests
from bs4 import BeautifulSoup
import tkintermapview
from tkinter import messagebox

login_data = {
    "ARafał": "Medica1",
    "RAndrzej": "Medica2",
    "MArtur": "Care1",
    "AMichał": "Care2",
    "KMarcin": "Lux1",
    "MKarol": "Lux2",
    "JMagda": "Marvit1",
    "MJoanna": "Marvit2",
    "OPaulina": "Prima1",
    "POliwia": "Prima2"
}

przychodnie = []


class Przychodnia:
    def __init__(self, nazwa, doktorzy, pacjenci, lokalizacja):
        self.nazwa = nazwa
        self.doktorzy = doktorzy
        self.pacjenci = pacjenci
        self.lokalizacja = lokalizacja
        self.wspolrzedne = self.get_wspolrzedne()
        self.marker = None

    def get_wspolrzedne(self) -> list:
        url: str = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(",", ".")),
            float(response_html.select('.longitude')[1].text.replace(",", "."))
        ]

    def usun_marker(self):
        if self.marker:
            self.marker.delete()


def lista_przychodni(listbox_lista_przychodni, map_widget):
    listbox_lista_przychodni.delete(0, END)
    for idx, przychodnia in enumerate(przychodnie):
        listbox_lista_przychodni.insert(idx,
                                        f'{przychodnia.nazwa}  {przychodnia.doktorzy} {przychodnia.pacjenci} {przychodnia.lokalizacja}')
        przychodnia.marker = map_widget.set_marker(przychodnia.wspolrzedne[0], przychodnia.wspolrzedne[1],
                                                   text=f"{przychodnia.nazwa}")


def dodaj_przychodnie(entry_nazwa, entry_doktorzy, entry_pacjenci, entry_lokalizacja, listbox_lista_przychodni,
                      map_widget):
    nazwa = entry_nazwa.get()
    doktorzy = entry_doktorzy.get()
    pacjenci = entry_pacjenci.get()
    lokalizacja = entry_lokalizacja.get()
    przychodnie.append(Przychodnia(nazwa, doktorzy, pacjenci, lokalizacja))
    lista_przychodni(listbox_lista_przychodni, map_widget)

    entry_nazwa.delete(0, END)
    entry_doktorzy.delete(0, END)
    entry_pacjenci.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_nazwa.focus()


def usun_przychodnie(listbox_lista_przychodni, map_widget):
    i = listbox_lista_przychodni.curselection()[0]
    przychodnie[i].marker.delete()
    przychodnie.pop(i)
    lista_przychodni(listbox_lista_przychodni, map_widget)


def pokaz_szczegoly_przychodni(listbox_lista_przychodni, label_nazwa_szczegoly_obiektu_wartosc,
                               label_doktorzy_szczegoly_obiektu_wartosc, label_pacjenci_szczegoly_obiektu_wartosc,
                               label_lokalizacja_szczegoly_obiektu_wartosc, map_widget):
    i = listbox_lista_przychodni.curselection()[0]
    przychodnia = przychodnie[i]
    label_nazwa_szczegoly_obiektu_wartosc.config(text=przychodnia.nazwa)
    label_doktorzy_szczegoly_obiektu_wartosc.config(text=przychodnia.doktorzy)
    label_pacjenci_szczegoly_obiektu_wartosc.config(text=przychodnia.pacjenci)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=przychodnia.lokalizacja)
    map_widget.set_position(przychodnia.wspolrzedne[0], przychodnia.wspolrzedne[1])
    map_widget.set_zoom(12)


def edytuj_przychodnie(listbox_lista_przychodni, entry_nazwa, entry_doktorzy, entry_pacjenci, entry_lokalizacja,
                       button_dodaj_przychodnie, map_widget):
    i = listbox_lista_przychodni.curselection()[0]
    przychodnia = przychodnie[i]
    przychodnia.usun_marker()
    entry_nazwa.insert(0, przychodnia.nazwa)
    entry_doktorzy.insert(0, przychodnia.doktorzy)
    entry_pacjenci.insert(0, przychodnia.pacjenci)
    entry_lokalizacja.insert(0, przychodnia.lokalizacja)
    button_dodaj_przychodnie.config(text="Zapisz zmiany",
                                    command=lambda: aktualizuj_przychodnie(i, entry_nazwa, entry_doktorzy,
                                                                           entry_pacjenci, entry_lokalizacja,
                                                                           button_dodaj_przychodnie,
                                                                           listbox_lista_przychodni, map_widget))


def aktualizuj_przychodnie(i, entry_nazwa, entry_doktorzy, entry_pacjenci, entry_lokalizacja, button_dodaj_przychodnie,
                           listbox_lista_przychodni, map_widget):
    przychodnia = przychodnie[i]
    przychodnia.nazwa = entry_nazwa.get()
    przychodnia.doktorzy = entry_doktorzy.get()
    przychodnia.pacjenci = entry_pacjenci.get()
    przychodnia.lokalizacja = entry_lokalizacja.get()
    przychodnia.wspolrzedne = przychodnia.get_wspolrzedne()
    lista_przychodni(listbox_lista_przychodni, map_widget)
    button_dodaj_przychodnie.config(text="Dodaj przychodnię",
                                    command=lambda: dodaj_przychodnie(entry_nazwa, entry_doktorzy, entry_pacjenci,
                                                                      entry_lokalizacja, listbox_lista_przychodni,
                                                                      map_widget))
    entry_nazwa.delete(0, END)
    entry_doktorzy.delete(0, END)
    entry_pacjenci.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_nazwa.focus()


def okno_przychodnie(root):
    global map_widget
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
                                                                               label_lokalizacja_szczegoly_obiektu_wartosc,
                                                                               map_widget))
    button_usun_obiekt = Button(ramka_lista_przychodni, text='Usuń obiekt',
                                command=lambda: usun_przychodnie(listbox_lista_przychodni, map_widget))
    button_edytuj_obiektu = Button(ramka_lista_przychodni, text='Edytuj obiekt',
                                   command=lambda: edytuj_przychodnie(listbox_lista_przychodni, entry_nazwa,
                                                                      entry_doktorzy, entry_pacjenci,
                                                                      entry_lokalizacja, button_dodaj_przychodnie,
                                                                      map_widget))

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
                                                                        entry_lokalizacja, listbox_lista_przychodni,
                                                                        map_widget))
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
    label_nazwa_szczegoly_obiektu.grid(row=1, column=0, )
    label_nazwa_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_doktorzy_szczegoly_obiektu.grid(row=1, column=2)
    label_doktorzy_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    label_pacjenci_szczegoly_obiektu.grid(row=1, column=4)
    label_pacjenci_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
    label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)

    global map_widget
    map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=500)
    map_widget.set_position(52.2, 21.0)
    map_widget.set_zoom(8)
    map_widget.grid(row=2, column=0, columnspan=8)


lekarze = []


class Lekarz:
    def __init__(self, imie, nazwisko, placowka, przynalezni_pacjenci, pochodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.placowka = placowka
        self.przynalezni_pacjenci = przynalezni_pacjenci
        self.pochodzenie = pochodzenie
        self.wspolrzedne = self.get_wspolrzedne()
        self.marker = None

    def get_wspolrzedne(self) -> list:
        url: str = f'https://pl.wikipedia.org/wiki/{self.pochodzenie}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(",", ".")),
            float(response_html.select('.longitude')[1].text.replace(",", "."))
        ]

    def usun_marker(self):
        if self.marker:
            self.marker.delete()


def lista_lekarzy(listbox_lista_lekarzy, map_widget):
    listbox_lista_lekarzy.delete(0, END)
    for idx, lekarz in enumerate(lekarze):
        listbox_lista_lekarzy.insert(idx,
                                     f'{lekarz.imie}  {lekarz.nazwisko} {lekarz.placowka} {lekarz.przynalezni_pacjenci} {lekarz.pochodzenie}')
        lekarz.marker = map_widget.set_marker(lekarz.wspolrzedne[0], lekarz.wspolrzedne[1],
                                              text=f"{lekarz.imie}")


def zatrudnij_doktora(entry_imie, entry_nazwisko, entry_placowka, entry_przynalezni_pacjenci, entry_pochodenie,
                      listbox_lista_lekarzy, map_widget):
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    placowka = entry_placowka.get()
    przynalezni_pacjenci = entry_przynalezni_pacjenci.get()
    pochodzenie = entry_pochodenie.get()
    lekarze.append(Lekarz(imie, nazwisko, placowka, przynalezni_pacjenci, pochodzenie))
    lista_lekarzy(listbox_lista_lekarzy, map_widget)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_placowka.delete(0, END)
    entry_przynalezni_pacjenci.delete(0, END)
    entry_pochodenie.delete(0, END)
    entry_imie.focus()


def zwolnij_doktora(listbox_lista_lekarzy, map_widget):
    i = listbox_lista_lekarzy.index(ACTIVE)
    lekarze[i].marker.delete()
    lekarze.pop(i)
    lista_lekarzy(listbox_lista_lekarzy, map_widget)


def informacje_o_doktorze(listbox_lista_lekarzy, label_imie_szczegoly_obiektu_wartosc,
                          label_nazwisko_szczegoly_obiektu_wartosc, label_placowka_szczegoly_obiektu_wartosc,
                          label_przynalezni_pacjenci_szczegoly_obiektu_wartosc,
                          label_pochodzenie_szczegoly_obietu_wartosc, map_widget):
    i = listbox_lista_lekarzy.curselection()[0]
    lekarz = lekarze[i]
    label_imie_szczegoly_obiektu_wartosc.config(text=lekarz.imie)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=lekarz.nazwisko)
    label_placowka_szczegoly_obiektu_wartosc.config(text=lekarz.placowka)
    label_przynalezni_pacjenci_szczegoly_obiektu_wartosc.config(text=lekarz.przynalezni_pacjenci)
    label_pochodzenie_szczegoly_obietu_wartosc.config(text=lekarz.pochodzenie)
    map_widget.set_position(lekarz.wspolrzedne[0], lekarz.wspolrzedne[1])
    map_widget.set_zoom(12)


def edytuj_doktora(listbox_lista_lekarzy, entry_imie, entry_nazwisko, entry_placowka, entry_przynalezni_pacjenci,
                   entry_pochodzenie,
                   button_zatrudnij_doktora, map_widget):
    i = listbox_lista_lekarzy.curselection()[0]
    lekarz = lekarze[i]
    lekarz.usun_marker()
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
                                                                       listbox_lista_lekarzy, map_widget))


def aktualizuj_doktora(i, entry_imie, entry_nazwisko, entry_placowka, entry_przynalezni_pacjenci, entry_pochodzenie,
                       button_zatrudnij_doktora,
                       listbox_lista_lekarzy, map_widget):
    lekarz = lekarze[i]
    lekarz.imie = entry_imie.get()
    lekarz.nazwisko = entry_nazwisko.get()
    lekarz.placowka = entry_placowka.get()
    lekarz.przynalezni_pacjenci = entry_przynalezni_pacjenci.get()
    lekarz.pochodzenie = entry_pochodzenie.get()
    lista_lekarzy(listbox_lista_lekarzy, map_widget)
    button_zatrudnij_doktora.config(text="Zaktualizuj dane o doktorze",
                                    command=lambda: zatrudnij_doktora(entry_imie, entry_nazwisko, entry_placowka,
                                                                      entry_przynalezni_pacjenci, entry_pochodzenie,
                                                                      listbox_lista_lekarzy, map_widget))
    entry_imie.delete(0, END),
    entry_nazwisko.delete(0, END),
    entry_placowka.delete(0, END),
    entry_przynalezni_pacjenci.delete(0, END),
    entry_pochodzenie.delete(0, END),
    entry_imie.focus()


def okno_lekarze(root):
    global map_widget
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
                                                                          label_pochodzenie_szczegoly_obiektu_wartosc,
                                                                          map_widget))
    button_zwolnij_doktora = Button(ramka_lista_lekarzy, text='Zwolnij doktora',
                                    command=lambda: zwolnij_doktora(listbox_lista_lekarzy, map_widget))
    button_edytuj_dane = Button(ramka_lista_lekarzy, text='Edytuj informacje o doktorze',
                                command=lambda: edytuj_doktora(listbox_lista_lekarzy, entry_imie,
                                                               entry_nazwisko, entry_placowka,
                                                               entry_przynalezni_pacjenci, entry_pochodzenie,
                                                               button_zatrudnij_doktora, map_widget))

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
                                                                        listbox_lista_lekarzy, map_widget))
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

    global map_widget
    map_widget = tkintermapview.TkinterMapView(ramka_informacje_o_doktorze, width=900, height=500)
    map_widget.set_position(52.2, 21.0)
    map_widget.set_zoom(8)
    map_widget.grid(row=2, column=0, columnspan=8)

from tkinter import *
import requests
import tkintermapview
from bs4 import BeautifulSoup

pacjenci = []


class Pacjent:
    def __init__(self, imie, nazwisko, przychodnia, lokalizacja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przychodnia = przychodnia
        self.lokalizacja = lokalizacja
        self.wspolrzedne = self.get_wspolrzedne()
        self.marker = None

    def get_wspolrzedne(self) -> list:
        url: str = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(",", ".")),
            float(response_html.select('.longitude')[1].text.replace(",", "."))
        ]

    def usun_marker(self):
        if self.marker:
            self.marker.delete()


def lista_pacjentow(listbox_lista_pacjentow, map_widget):
    listbox_lista_pacjentow.delete(0, END)
    for idx, pacjent in enumerate(pacjenci):
        listbox_lista_pacjentow.insert(idx,
                                       f'{pacjent.imie}  {pacjent.nazwisko} {pacjent.przychodnia} {pacjent.lokalizacja}')
        pacjent.marker = map_widget.set_marker(pacjent.wspolrzedne[0], pacjent.wspolrzedne[1],
                                               text=f"{pacjent.imie}")


def dodaj_pacjenta(entry_imie, entry_nazwisko, entry_przychodnia, entry_lokalizacja, listbox_lista_pacjentow,
                   map_widget):
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    przychodnia = entry_przychodnia.get()
    lokalizacja = entry_lokalizacja.get()
    pacjenci.append(Pacjent(imie, nazwisko, przychodnia, lokalizacja))
    lista_pacjentow(listbox_lista_pacjentow, map_widget)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_przychodnia.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def usun_pacjenta(listbox_lista_pacjentow, map_widget):
    i = listbox_lista_pacjentow.curselection()[0]
    pacjenci[i].marker.delete()
    pacjenci.pop(i)
    lista_pacjentow(listbox_lista_pacjentow, map_widget)


def pokaz_szczegoly_pacjenta(listbox_lista_pacjentow, label_imie_szczegoly_obiektu_wartosc,
                             label_nazwisko_szczegoly_obiektu_wartosc, label_przychodnia_szczegoly_obiektu_wartosc,
                             label_lokalizacja_szczegoly_obiektu_wartosc, map_widget):
    i = listbox_lista_pacjentow.curselection()[0]
    pacjent = pacjenci[i]
    label_imie_szczegoly_obiektu_wartosc.config(text=pacjent.imie)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=pacjent.nazwisko)
    label_przychodnia_szczegoly_obiektu_wartosc.config(text=pacjent.przychodnia)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=pacjent.lokalizacja)
    map_widget.set_position(pacjent.wspolrzedne[0], pacjent.wspolrzedne[1])
    map_widget.set_zoom(12)


def edytuj_pacjenta(listbox_lista_pacjentow, entry_imie, entry_nazwisko, entry_przychodnia, entry_lokalizacja,
                    button_dodaj_pacjenta, map_widget):
    i = listbox_lista_pacjentow.curselection()[0]
    pacjent = pacjenci[i]
    pacjent.usun_marker()
    entry_imie.insert(0, pacjent.imie)
    entry_nazwisko.insert(0, pacjent.nazwisko)
    entry_przychodnia.insert(0, pacjent.przychodnia)
    entry_lokalizacja.insert(0, pacjent.lokalizacja)
    button_dodaj_pacjenta.config(text="Zapisz zmiany",
                                 command=lambda: aktualizuj_pacjenta(i, entry_imie, entry_nazwisko,
                                                                     entry_przychodnia, entry_lokalizacja,
                                                                     button_dodaj_pacjenta,
                                                                     listbox_lista_pacjentow, map_widget))


def aktualizuj_pacjenta(i, entry_imie, entry_nazwisko, entry_przychodnia, entry_lokalizacja, button_dodaj_pacjenta,
                        listbox_lista_pacjentow, map_widget):
    pacjent = pacjenci[i]
    pacjent.imie = entry_imie.get()
    pacjent.nazwisko = entry_nazwisko.get()
    pacjent.przychodnia = entry_przychodnia.get()
    pacjent.lokalizacja = entry_lokalizacja.get()
    pacjent.wspolrzedne = pacjent.get_wspolrzedne()
    lista_pacjentow(listbox_lista_pacjentow, map_widget)
    button_dodaj_pacjenta.config(text="Dodaj przychodnię",
                                 command=lambda: dodaj_pacjenta(entry_imie, entry_nazwisko, entry_przychodnia,
                                                                entry_lokalizacja, listbox_lista_pacjentow,
                                                                map_widget))
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_przychodnia.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def okno_pacjenci(root):
    global map_widget
    pacjenci_root = Toplevel(root)
    pacjenci_root.title("Lista pacjentów")
    pacjenci_root.geometry("1024x720")

    # ramki do porządkowania struktury
    ramka_lista_pacjentow = Frame(pacjenci_root)
    ramka_formularz = Frame(pacjenci_root)
    ramka_szczegoly_obiektu = Frame(pacjenci_root)

    ramka_lista_pacjentow.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista_placowek
    label_lista_pacjentow = Label(ramka_lista_pacjentow, text="Lista przychodni: ")
    listbox_lista_pacjentow = Listbox(ramka_lista_pacjentow, width=50)
    button_pokaz_szczegoly = Button(ramka_lista_pacjentow, text="Pokaż szczegóły",
                                    command=lambda: pokaz_szczegoly_pacjenta(listbox_lista_pacjentow,
                                                                             label_imie_szczegoly_obiektu_wartosc,
                                                                             label_nazwisko_szczegoly_obiektu_wartosc,
                                                                             label_przychodnia_szczegoly_obiektu_wartosc,
                                                                             label_lokalizacja_szczegoly_obiektu_wartosc,
                                                                             map_widget))
    button_usun_pacjenta = Button(ramka_lista_pacjentow, text='Usuń pacjenta',
                                  command=lambda: usun_pacjenta(listbox_lista_pacjentow, map_widget))
    button_edytuj_pacjenta = Button(ramka_lista_pacjentow, text='Edytuj pacjenta',
                                    command=lambda: edytuj_pacjenta(listbox_lista_pacjentow, entry_imie,
                                                                    entry_nazwisko, entry_przychodnia,
                                                                    entry_lokalizacja, button_dodaj_pacjenta,
                                                                    map_widget))

    label_lista_pacjentow.grid(row=0, column=0, columnspan=3)
    listbox_lista_pacjentow.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly.grid(row=2, column=0)
    button_usun_pacjenta.grid(row=2, column=1)
    button_edytuj_pacjenta.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Formularz")
    label_imie = Label(ramka_formularz, text="Imię: ")
    label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
    label_przychodnia = Label(ramka_formularz, text="Przychodnia: ")
    label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")

    entry_imie = Entry(ramka_formularz)
    entry_nazwisko = Entry(ramka_formularz)
    entry_przychodnia = Entry(ramka_formularz)
    entry_lokalizacja = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_imie.grid(row=1, column=0, sticky=W)
    label_nazwisko.grid(row=2, column=0, sticky=W)
    label_przychodnia.grid(row=3, column=0, sticky=W)
    label_lokalizacja.grid(row=4, column=0, sticky=W)

    entry_imie.grid(row=1, column=1)
    entry_nazwisko.grid(row=2, column=1)
    entry_przychodnia.grid(row=3, column=1)
    entry_lokalizacja.grid(row=4, column=1)

    button_dodaj_pacjenta = Button(ramka_formularz, text="Dodaj pacjenta",
                                   command=lambda: dodaj_pacjenta(entry_imie, entry_nazwisko, entry_przychodnia,
                                                                  entry_lokalizacja, listbox_lista_pacjentow,
                                                                  map_widget))
    button_dodaj_pacjenta.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu
    label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Informacje o pacjencie: ")
    label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Imię: ")
    label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
    label_przychodnia_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Przychodnia: ")
    label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja: ")

    label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_przychodnia_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
    label_imie_szczegoly_obiektu.grid(row=1, column=0, )
    label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
    label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    label_przychodnia_szczegoly_obiektu.grid(row=1, column=4)
    label_przychodnia_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
    label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)

    global map_widget
    map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=500)
    map_widget.set_position(52.2, 21.0)
    map_widget.set_zoom(8)
    map_widget.grid(row=2, column=0, columnspan=8)

def logowanie():
    login_window = Tk()
    login_window.title("Logowanie")
    login_window.geometry("300x150")

    label_login = Label(login_window, text="Login:")
    label_login.pack(pady=5)
    entry_login = Entry(login_window)
    entry_login.pack(pady=5)

    label_haslo = Label(login_window, text="Hasło:")
    label_haslo.pack(pady=5)
    entry_haslo = Entry(login_window, show="*")
    entry_haslo.pack(pady=5)

    def validate_login():
        login = entry_login.get()
        haslo = entry_haslo.get()
        print(f"Login: {login}, Hasło: {haslo}")  # Dodaj do debugowania
        if login in login_data and login_data[login] == haslo:
            print("Dostęp przyznany")
            login_window.destroy()
            main_window()
        else:
            print("Błędne dane logowania. Spróbuj ponownie.")
            messagebox.showerror("Błąd logowania", "Błędne dane logowania. Spróbuj ponownie.")  # Informacja zwrotna

    button_login = Button(login_window, text="Zaloguj", command=validate_login)
    button_login.pack(pady=20)

    login_window.mainloop()


def main_window():
    root = Tk()
    root.title("Przychodnie w pobliżu")
    root.geometry("800x500")

    label = Label(root, text="Wybierz opcję:")
    label.grid(row=0, column=0, columnspan=3)

    button1 = Button(root, text="Lista przychodni", command=lambda: okno_przychodnie(root))
    button1.grid(row=1, column=0)

    button2 = Button(root, text="Lista lekarzy", command=lambda: okno_lekarze(root))
    button2.grid(row=1, column=1)

    button3 = Button(root, text="Lista pacjentów", command=lambda: okno_pacjenci(root))
    button3.grid(row=1, column=2)

    root.mainloop()


logowanie()
