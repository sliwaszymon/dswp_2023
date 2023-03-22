zdanie = input("Wpisz jakieś zdanie: ")
lista = zdanie.split()
lista = sorted(lista, key=len)
print(lista)