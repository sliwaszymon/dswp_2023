import math
from typing import Union, Tuple

Num = Union[int, float]
DeltaReturn = Union[Num, Tuple]

def row_kwadratowe(a: Num, b: Num, c: Num) -> DeltaReturn:
    delta: float = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x: float = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1: float = (- b - math.sqrt(delta)) / (2 * a)
        x2: float = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))