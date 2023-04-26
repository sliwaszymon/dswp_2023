import random
import math
import re

# SZYMON ŚLIWA 155471 

def zadanie_1(zdanie: str) -> dict:
    digit = [x for x in list(zdanie) if x.isdigit()]
    lower = [x for x in list(zdanie) if x.islower()]
    upper = [x for x in list(zdanie) if x.isupper()]
    ans = {
        'lower': len(lower),
        'upper': len(upper),
        'digits': len(digit)
    }
    return ans

def zadanie_2(n: int):
    text = str(input("Podaj tekst: "))
    print(text*n)

def zadanie_3() -> str:
    text = ''
    while len(text.split(' ')) < 3:
        text = str(input('Podaj tekst min. 3 wyrazy: '))
    lista = text.split(' ')
    wyrazy = []
    for x in range(3):
        wyrazy.append(lista.pop(random.randint(0, len(lista)-1)))
    text = " ".join(wyrazy)
    return text.capitalize()

def zadanie_4():
    return [math.log2(i**2) for i in range(1,17)]

def zadanie_5(lista: list):
    return [f'{x:0>{len(str(max(lista)))}}' for x in lista]

def zadanie_6(tekst: str, max_ilosc_znakow: int) -> str: 
    temp = list(tekst)[:max_ilosc_znakow]
    if list(tekst)[:max_ilosc_znakow+1] == ' ':
        return ''.join(temp)
    else:
        temp = temp[::-1]
        while temp[0] != ' ':
            temp.pop(0)
    return ''.join(temp[::-1])


def zadanie_7(prefix: str, amount: int):
    return {f'{prefix}_{x:0>{len(str(amount))}}' for x in range(1, amount+1)}

def zadanie_8(tekst: str):
    regex = r'\d*\.\d+|\d+'
    ans = re.findall(regex, tekst)
    return [float(x) if '.' in x else int(x) for x in ans]

def main():
    # print(zadanie_1('ala To kotA 1'))
    # zadanie_2(3)
    # print(zadanie_3())
    # print(zadanie_4())
    # print(zadanie_5([1, 23, 564]))
    print(zadanie_6('ala ma kota', 6))
    # print(zadanie_7('prefix', 100))
    # print(zadanie_8('Jego nick to Bob87 a jego kdratio to 1.411'))

if __name__ == '__main__':
    main()
