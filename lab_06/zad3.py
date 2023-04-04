def foo(lista, najwieksza=True):
    if not all([(isinstance(liczba, int) or isinstance(liczba, float))for liczba in lista]):
        return False
    
    ans = lista[0]
    if najwieksza:
        for x in lista[1:]:
            if x > ans: ans = x
        return ans
    else:
        for x in lista[1:]:
            if x < ans: ans = x
        return ans


lista = [1,7,21,4,8,-15]
lista2 = [1,7,21,4,'a',8,-15]

print(foo(lista))
print(foo(lista, False))
print(foo(lista2))