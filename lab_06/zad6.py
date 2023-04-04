zdanie = "Ala ma kota"

def foo(zdanie):
    literki = [list(wyraz)[::-1] for wyraz in zdanie.split(" ")]
    odwrotnie = ["".join(litery) for litery in literki]
    return " ".join(odwrotnie)

print(foo(zdanie))