def foo(lista: list[int|float]) -> list[int|float]:
    lista.sort(reverse=True)
    limiter = len(lista) // 10 + 1 if len(lista)%2 == 1 or len(lista) < 10 else len(lista) // 10
    return lista[:limiter]

print(foo([10,20,4,1,7,14]))
print(foo([10,20,4,1,7,14,7,11,23,41,100,12,43,21,4,112,5,2,1,3,5,6,7]))