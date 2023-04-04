import codecs

def foo(domena):
    with open('maile.txt', 'w') as maile:
        with codecs.open('osoby.txt', 'r', 'utf-8-sig') as osoby:
            for osoba in osoby:
                os = osoba.lower().replace('\n', '').replace('\r', '').replace('ą', 'a').replace('ę', 'e').replace('ó', 'o').replace('ś', 's').replace('ł', 'l').replace('ż', 'z').replace('ź', 'z').replace('ń', 'n').split(' ')
                maile.write(f'{os[0]}.{os[1]}@{domena}\n')

foo('bystrzacy.pl')