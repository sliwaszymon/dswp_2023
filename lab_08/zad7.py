import random
from collections import deque
from zad6 import create_kolo_fortuny

def spinit(kolo_fortuny: deque):
    kolo_fortuny.rotate(random.randint(0, len(kolo_fortuny)**2))
    print(f'Wheel: {kolo_fortuny}')


kolo_fortuny = create_kolo_fortuny(2,1,3,7,22,43,21,34,5,87,65,43,21,39)
warunek_wygranej = random.choice(kolo_fortuny)

print(f'Warunkiem wygranej jest {warunek_wygranej}')

while kolo_fortuny[0] != warunek_wygranej:
    spinit(kolo_fortuny)