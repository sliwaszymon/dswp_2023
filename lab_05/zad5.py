import random

def foo() -> list[tuple[str, str]]:
    n: int = int(input("Podaj liczbę rzutów: "))
    dictio: dict = {}
    for x in range(n):
        los: int = random.randint(1, 6) 
        try:
            dictio[los] += 1
        except KeyError:
            dictio[los] = 1
    
    return [(f'oczka: {key}', f'rzutów: {dictio[key]}') for key in dictio.keys()]

print(foo())