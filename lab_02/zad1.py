ciag = input('Podaj ciąg wartości oddzielanych jakimś separatorem: ')
separator_zrodlowy = input('Jakim separatorem oddzielono dane? ')
separator_docelowy = input('Jakim separatorem zlaczyc dane? ')

print(ciag)

ciag = ciag.split(separator_zrodlowy)
print(ciag)
ciag = separator_docelowy.join(ciag)
print(ciag)

# po co jak istnieje .replace()?????????????/