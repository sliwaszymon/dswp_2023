import csv
from collections import namedtuple

with open('../lab_06/zamowienia.csv', encoding="utf8") as file:
    reader = csv.reader(file, delimiter=';')
    line = next(reader)
    labels = [pole.lower().replace(' ', '_') for pole in line]
    temp_tuple = namedtuple('tuple', labels)
    krotki = []
    for i, wiersz in enumerate(reader):
        if i == 10:
            break
        wartosci_pol = wiersz[:len(labels)]
        krotka = temp_tuple._make(wartosci_pol)
        krotki.append(krotka)

print(krotki)