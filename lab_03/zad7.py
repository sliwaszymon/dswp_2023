from string import ascii_lowercase, digits
ciag = str(input('Podaj jakiś ciąg znaków: '))

znaki = list(dict.fromkeys(list(ciag.casefold())))

print(f'{len([x for x in znaki if x in ascii_lowercase]) / len(ascii_lowercase) * 100:.2f} % liter z string.ascii_lowercase i', 
      f'{len([x for x in znaki if x in digits]) / len(digits) * 100:.2f} % cyfr z string.digits znajduje się we wprowadzonym tekście')
