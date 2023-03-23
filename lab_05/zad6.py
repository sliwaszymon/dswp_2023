def sortowanie_wyrazow(*wyrazy: str) -> list[str] | bool:
    if len(wyrazy) == 0:
        return False
    else:
        wyrazy = sorted(wyrazy)
        return wyrazy

print(sortowanie_wyrazow())
print(sortowanie_wyrazow('ala', 'ma', 'kotów', 'sto', 'ale', 'psów', 'wcale'))