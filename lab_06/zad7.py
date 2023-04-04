from itertools import chain
import random



def foo():
    karta = [2,3,4,5,6,7,8,9,10,'Walet', 'Dama', 'Król', 'AS']
    kolor = ['Pik', 'Kier', 'Trefl', 'Karo']

    talia = list(chain.from_iterable([[f'{y} {x}' for y in karta] for x in kolor]))

    gracze = {
        'Adrian': [],
        'Janek': [],
        'Szymon': [],
        'Marcin': []
    }

    # Tak rozdaje każdemu po 1 i tak w kółko
    for x in range(5):
        for gracz in gracze.keys():
            gracze[gracz].append(talia.pop(random.randint(0, len(talia)-1)))

    # A tak jednemu 5, drugiemu 5 itd
    # for gracz in gracze.keys():
    #     for x in range(5):
    #         gracze[gracz].append(talia.pop(random.randint(0, len(talia)-1)))
    #     print(f'{gracz}: {gracze[gracz]}')
    # może mniej "fair" ale nie trzeba kolejnej pętli do wypisywania "ręki"

    for gracz in gracze.keys():  
        print(f'{gracz}: {gracze[gracz]}')


foo()