import sys

def foo(x):
    lista = list(str(x).replace('\n', ''))
    lista.reverse()
    dictio = {}
    key = 1 
    for x in range(len(lista)):
        dictio[key] = lista[x]
        key *= 10
    
    return dictio

print("Podaj liczbę całkowitą: ")
liczba = sys.stdin.readline()

dictio = foo(liczba)
keys = list(dictio.keys())
keys.reverse()
adds = [f'{key} * {dictio[key]}' for key in keys]
print(adds)
text = ' + '.join(adds)
text = text + "."

sys.stdout.write(f'Podaną liczbę można zapisać jako: ')
sys.stdout.write(text)


# TAK, WIDZE JAK BARDZO ŁOPATOLOGICZNE TO JEST
# ALE NA PRAWDE NIE MAM CZASU SZUKAĆ OPTYMALNEGO ROZWIĄZANIA
# ZROBIŁEM PIERWSZE LEPSZE DZIAŁAJĄCE