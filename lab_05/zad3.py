zdanie = input("Podaj zdanie: ")
lista = zdanie.split(" ")

returned = [(slowo, [ord(letter) for letter in list(slowo)]) for slowo in lista]
print(returned)