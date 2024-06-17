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
    {"Andrzej", "Rafał","Maciej Marek, Miłosz Wojciech", "Medica Kobyłka","Kobyłka"},
    {"Rafał", "Andrzej", "Marek Maciej, Wojciech Miłosz", "Medica Kobyłka", "Wołomin"},
    {"Michał", "Artur", "Anna Maria, Aleksandra Leokadia", "Care Ząbki", "Wałbrzych"},
    {"Artur", "Michał","Maria Anna, Leokadia Aleksandra" ,  "Care Ząbki", "Lublin"},
    {"Karol", "Marcin","Agnieszka Elżbieta, Paweł Gaweł" , "Lux Słupno", "Warszawa"},
    {"Marcin", "Karol","Elżbieta Agnieszka, Gaweł Paweł" , "Lux Słupno", "Łódź"},
    {"Joanna", "Magda", "Andrzej Kacper, Adrianna Urszula", "Marvit Wyszków", "Wyszków"},
    {"Magda", "Joanna","Kacper Andrzej, Urszula Adrianna" , "Marvit Wyszków", "Jadów"},
    {"Oliwia", "Paulina","Jakub Piotr, Janina Weronika" , "Prima Tłuszcz", "Kołobrzeg"},
    {"Paulina", "Oliwia","Piotr Jakub, Weronika Janina", "Prima Tłuszcz", "Międzyzdroje"},
]

wszyscy_pacjenci: list =[
    ("Maciej", "nazwisko: Marek", "przychodnia: Medica Kobyłka", "pochodzenie: Kobyłka"),
    ("Marek", "nazwisko: Maciej", "przychodnia: Medica Kobyłka", "pochodzenie: Wołomin"),
    ("Miłosz", "nazwisko: Wojciech", "przychodnia: Medica Kobyłka", "pochodzenie: Zielonka"),
    ("Wojciech", "nazwisko: Miłosz", "przychodnia: Medica Kobyłka", "pochodzenie: Nadma"),
    ("Anna", "nazwisko: Maria", "przychodnia: Care Ząbki", "pochodzenie: Ząbki"),
    ("Maria", "nazwisko: Anna", "przychodnia: Care Ząbki", "pochodzenie: Warszawa"),
    ("Aleksandra", "nazwisko: Leokadia", "przychodnia: Care Ząbki", "pochodzenie: Radzymin"),
    ("Leokadia", "nazwisko: Aleksandra", "przychodnia: Care Ząbki", "pochodzenie: Marki"),
    ("Agnieszka", "nazwisko: Elżbieta", "przychodnia: Lux Słupno", "pochodzenie: Słupno_(gmina)"),
    ("Elżbieta", "nazwisko: Agnieszka", "przychodnia: Lux Słupno", "pochodzenie: Cegielnia_(powiat_wołomiński)"),
    ("Paweł", "nazwisko: Gaweł", "przychodnia: Lux Słupno", "pochodzenie: Stary_Dybów"),
    ("Gaweł", "nazwisko: Paweł", "przychodnia: Lux Słupno", "pochodzenie: Stary_Kraszew"),
    ("Andrzej", "nazwisko: Kacper", "przychodnia: Marvit Wyszków", "pochodzenie: Wyszków"),
    ("Kacper", "nazwisko: Andrzej", "przychodnia: Marvit Wyszków", "pochodzenie: Niegów"),
    ("Adrianna", "nazwisko: Urszula", "przychodnia: Marvit Wyszków", "pochodzenie: Natalin_(powiat_wyszkowski)"),
    ("Urszula", "nazwisko: Adrianna", "przychodnia: Marvit Wyszków", "pochodzenie: Trzcianka_(powiat_wyszkowski)"),
    ("Jakub", "nazwisko: Piotr", "przychodnia: " "Prima Tłuszcz", "pochodzenie: Tłuszcz_(miasto)"),
    ("Piotr", "nazwisko: Jakub", "przychodnia: Prima Tłuszcz", "pochodzenie: Jadów"),
    ("Janina", "nazwisko: Weronika", "przychodnia: Prima Tłuszcz", "pochodzenie: Klembów"),
    ("Weronika", "nazwisko: Janina", "przychodnia: Prima Tłuszcz", "pochodzenie: Wójty")
]