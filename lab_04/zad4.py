from this import d

s = input("Podaj zdanie: ")
print("".join([d.get(c, c) for c in s]))