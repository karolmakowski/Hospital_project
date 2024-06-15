doktorzy_Medica: list = [
    {"dr. Andrzej Rafał", "dr. Rafał Andrzej"}
]
pacjenci_Medica: list = [
    {"Maciej Marek", "Marek Maciej", "Miłosz Wojciech", "Wojciech Miłosz"}
]
pacjenci_Andrzej: list = [
    {"Maciej Marek", "Miłosz Wojciech"}
]
pacjenci_Rafal: list = [
    {"Marek Maciej", "Wojciech Miłosz"}
]
doktorzy_Care: list = [
    {"dr. Michał Artur", "dr. Artur Michał"}
]
pacjenci_Care: list = [
    {"Anna Maria", "Maria Anna", "Aleksandra Leokadia", "Leokadia Aleksandra"}
]
pacjenci_Michal: list = [
    {"Anna Maria", "Aleksandra Leokadia"}
]
pacjenci_Artur: list = [
    {"Maria Anna", "Leokadia Aleksandra"}
]
doktorzy_Lux: list = [
    {"dr. Karol Marcin", "dr. Marcin Karol"}
]
pacjenci_Lux: list = [
    {"Agnieszka Elżbieta", "Elżbieta Agnieszka", "Paweł Gaweł", "Gaweł Paweł"}
]
pacjenci_Karol: list = [
    {"Agnieszka Elżbieta", "Paweł Gaweł"}
]
pacjenci_Marcin: list = [
    {"Elżbieta Agnieszka", "Gaweł Paweł"}
]
doktorzy_Marvit: list = [
    {"dr. Joanna Magda", "dr. Magda Joanna"}
]
pacjenci_Marvit: list = [
    {"Andrzej Kacper", "Kacper Andrzej", "Adrianna Urszula", "Urszula Adrianna"}
]
pacjenci_Joanna: list = [
    {"Andrzej Kacper", "Adrianna Urszula"}
]
pacjenci_Magda: list = [
    {"Kacper Andrzej", "Urszula Adrianna"}
]
doktorzy_Prima: list = [
    {"dr. Oliwia Paulina", "dr. Paulina Oliwia"}
]
pacjenci_Prima: list = [
    {"Jakub Piotr", "Piotr Jakub", "Janina Weronika", "Weronika Janina"}
]
pacjenci_Oliwia: list = [
    {"Jakub Piotr", "Janina Weronika"}
]
pacjenci_Paulina: list = [
    {"Piotr Jakub", "Weronika Janina"}
]
wszystkie_przychodnie: list = [

    {"nazwa: ": "Medica Kobyłka", "doktorzy: ": doktorzy_Medica, "pacjenci: ": pacjenci_Medica,
     'lokalizacja: ': 'Kobyłka'},
    {"nazwa: ": "Care Ząbki", "doktorzy: ": doktorzy_Care, "pacjenci: ": pacjenci_Care, "lokalizacja: ": "Ząbki"},
    {"nazwa: ": "Lux Słupno", "doktorzy: ": doktorzy_Lux, "pacjenci: ": pacjenci_Lux,
     "lokalizacja: ": "Słupno_(gmina)"},
    {"nazwa: ": "Marvit Wyszków", "doktorzy: ": doktorzy_Marvit, "pacjenci: ": pacjenci_Marvit,
     "lokalizacja: ": "Wyszków"},
    {"nazwa: ": "Prima Tłuszcz", "doktorzy: ": doktorzy_Prima, "pacjenci: ": pacjenci_Prima,
     "lokalizacja: ": "Tłuszcz_(miasto)"}

]

wszyscy_doktorzy: list = [
    {"imię: ": "Andrzej", "nazwisko: ": "Rafał", "przynależni pacjenci: ": pacjenci_Andrzej, "placowka: ": "Medica Kobyłka", "pochodzenie: ": "Kobyłka"},
    {"imię: ": "Rafał", "nazwisko: ": "Andrzej", "przynależni pacjenci: ": pacjenci_Rafal, "placowka: ": "Medica Kobyłka", "pochodzenie: ": "Wołomin"},
    {"imię: ": "Michał", "nazwisko: ": "Artur", "przynależni pacjenci: ": pacjenci_Michal, "placowka: ": "Care Ząbki", "pochodzenie: ": "Wałbrzych"},
    {"imię: ": "Artur", "nazwisko: ": "Michał", "przynależni pacjenci: ": pacjenci_Artur, "placowka: ": "Care Ząbki", "pochodzenie: ": "Lublin"},
    {"imię: ": "Karol", "nazwisko: ": "Marcin", "przynależni pacjenci: ": pacjenci_Karol, "placowka: ": "Lux Słupno", "pochodzenie: ": "Warszawa"},
    {"imię: ": "Marcin", "nazwisko: ": "Karol", "przynależni pacjenci: ": pacjenci_Marcin, "placowka: ": "Lux Słupno", "pochodzenie: ": "Łódź"},
    {"imię: ": "Joanna", "nazwisko: ": "Magda", "przynależni pacjenci: ": pacjenci_Joanna, "placowka: ": "Marvit Wyszków", "pochodzenie: ": "Wyszków"},
    {"imię: ": "Magda", "nazwisko: ": "Joanna", "przynależni pacjenci: ": pacjenci_Magda, "placowka: ": "Marvit Wyszków", "pochodzenie: ": "Jadów"},
    {"imię: ": "Oliwia", "nazwisko: ": "Paulina", "przynależni pacjenci: ": pacjenci_Oliwia, "placowka: ": "Prima Tłuszcz", "pochodzenie: ": "Kołobrzeg"},
    {"imię: ": "Paulina", "nazwisko: ": "Oliwia", "przynależni pacjenci: ": pacjenci_Paulina, "placowka: ": "Prima Tłuszcz", "pochodzenie: ": "Międzyzdroje"},
]

wszyscy_pacjenci: list =[
    {"imię: ": "Maciej", "nazwisko: ": "Marek", "przychodnia: ": "Medica Kobyłka", "pochodzenie: ": "Kobyłka"},
    {"imię: ": "Marek", "nazwisko: ": "Maciej", "przychodnia: ": "Medica Kobyłka", "pochodzenie: ": "Wołomin"},
    {"imię: ": "Miłosz", "nazwisko: ": "Wojciech", "przychodnia: ": "Medica Kobyłka", "pochodzenie: ": "Zielonka"},
    {"imię: ": "Wojciech", "nazwisko: ": "Miłosz", "przychodnia: ": "Medica Kobyłka", "pochodzenie: ": "Nadma"},
    {"imię: ": "Anna", "nazwisko: ": "Maria", "przychodnia: ": "Care Ząbki", "pochodzenie: ": "Ząbki"},
    {"imię: ": "Maria", "nazwisko: ": "Anna", "przychodnia: ": "Care Ząbki", "pochodzenie: ": "Warszawa"},
    {"imię: ": "Aleksandra", "nazwisko: ": "Leokadia", "przychodnia: ": "Care Ząbki", "pochodzenie: ": "Radzymin"},
    {"imię: ": "Leokadia", "nazwisko: ": "Aleksandra", "przychodnia: ": "Care Ząbki", "pochodzenie: ": "Marki"},
    {"imię: ": "Agnieszka", "nazwisko: ": "Elżbieta", "przychodnia: ": "Lux Słupno", "pochodzenie: ": "Słupno_(gmina)"},
    {"imię: ": "Elżbieta", "nazwisko: ": "Agnieszka", "przychodnia: ": "Lux Słupno", "pochodzenie: ": "Cegielnia_(powiat_wołomiński)"},
    {"imię: ": "Paweł", "nazwisko: ": "Gaweł", "przychodnia: ": "Lux Słupno", "pochodzenie: ": "Stary_Dybów"},
    {"imię: ": "Gaweł", "nazwisko: ": "Paweł", "przychodnia: ": "Lux Słupno", "pochodzenie: ": "Stary_Kraszew"},
    {"imię: ": "Andrzej", "nazwisko: ": "Kacper", "przychodnia: ": "Marvit Wyszków", "pochodzenie: ": "Wyszków"},
    {"imię: ": "Kacper", "nazwisko: ": "Andrzej", "przychodnia: ": "Marvit Wyszków", "pochodzenie: ": "Niegów"},
    {"imię: ": "Adrianna", "nazwisko: ": "Urszula", "przychodnia: ": "Marvit Wyszków", "pochodzenie: ": "Natalin_(powiat_wyszkowski)"},
    {"imię: ": "Urszula", "nazwisko: ": "Adrianna", "przychodnia: ": "Marvit Wyszków", "pochodzenie: ": "Trzcianka_(powiat_wyszkowski)"},
    {"imię: ": "Jakub", "nazwisko: ": "Piotr", "przychodnia: ": "Prima Tłuszcz", "pochodzenie: ": "Tłuszcz_(miasto)},
    {"imię: ": "Piotr", "nazwisko: ": "Jakub", "przychodnia: ": "Prima Tłuszcz", "pochodzenie: ": "Jadów"},
    {"imię: ": "Janina", "nazwisko: ": "Weronika", "przychodnia: ": "Prima Tłuszcz", "pochodzenie: ": "Klembów"},
    {"imię: ": "Weronika", "Janina: ": "Weronika", "przychodnia: ": "Prima Tłuszcz", "pochodzenie: ": "Wójty"},
]