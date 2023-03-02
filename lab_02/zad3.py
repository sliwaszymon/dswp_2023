from zad2 import zmienna

imie, nazwisko = "Szymon", "Śliwa"

litera_1, litera_2 = imie[2], nazwisko[3]
liczba_liter1, liczba_liter2 = zmienna.count(litera_1), zmienna.count(litera_2)

print(f'W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}')