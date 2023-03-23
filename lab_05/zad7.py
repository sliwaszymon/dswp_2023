def foo(**wyniki) -> int:
    returned: int = 0
    for wynik in wyniki:
        returned += wyniki[wynik]
    return returned

print(foo(zawisza=20, lech= 14, legia=2137))