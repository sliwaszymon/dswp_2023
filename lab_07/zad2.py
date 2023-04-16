def foo() -> list[str]:
    lista = str(input('Wprowadź wyrazy oddzielone spacją: ')).split(' ')
    return list(sorted(lista, key=lambda x: len(x)))

print(foo())