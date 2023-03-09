import zad1

lista = zad1.lista + zad1.lista2
print(lista)
lista.insert(0, 0)
print(lista)

lista2 = lista.copy()
lista2.sort(reverse=True)
print(lista)
print(lista2)