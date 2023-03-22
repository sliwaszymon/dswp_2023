text = input("Podaj liczbę: ")

try:
    int(text)
except: 
    print("Nie da się rzutować na int")
else:
    print("Da się rzutować na int")

try:
    float(text)
except:
    print("Nie da się rzutować na float")
else:
    print("Da się rzutować na float")