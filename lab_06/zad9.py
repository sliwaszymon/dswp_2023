import random
import codecs

hasla = []
with codecs.open('hasla.txt', 'r', 'utf-8-sig') as h:
    for line in h:
        hasla.append(line.replace('\n', '').replace('\r', ''))


haslo = hasla.pop(random.randint(0, len(hasla)-1))

def foo(haslo):
    wygrana = False
    haslo_ukryte = [' ' if x==' ' else '_' for x in haslo]
    haslo_ukryte = "".join(haslo_ukryte)
    
    print(haslo_ukryte)
    while not wygrana:
        l = str(input("Podaj literę lub hasło: "))
        if len(l) > 1:
            if l==haslo:
                print(f'Brawo wygrałeś, hasło to {l}')
                break
            else:
                print('Hasło nie jest poprawne')
        else:
            for index in range(len(haslo_ukryte)):
                if haslo[index] == l:
                    print(f'litera {l} znajduje się w haśle')
                    haslo_ukryte = list(haslo_ukryte)
                    haslo_ukryte[index] = l
                    haslo_ukryte = "".join(haslo_ukryte)

        if haslo_ukryte == haslo:
            print(f'Brawo wygrałeś, hasło to {haslo_ukryte}')
            wygrana = True
        if not wygrana:
            print(haslo_ukryte)


foo(haslo)