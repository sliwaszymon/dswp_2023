lista = [x for x in range(1, 11)]
if __name__ == '__main__':
    print(lista)

lista, lista2 = lista[:5], lista[5:]
if __name__ == '__main__':
    print(lista)
    print(lista2)