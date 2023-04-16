import codecs
from datetime import datetime

lista = []
with codecs.open('../lab_06/zamowienia.csv', 'r', 'utf-8-sig') as f:
    for line in f:
        lista.append(line.replace('\n', '').replace('\r', '').replace(' z\x88', '').split(';'))

# zamiana przecinka na kropke
def zamiana(line):
    line[len(line)-1] = line[len(line)-1].replace(',','.').replace(' ', '')
    line[2] = datetime.strptime(line[2], '%d.%m.%Y').strftime('%Y-%m-%d')
    return line
lista = lista[0] + list(map(lambda x: zamiana(x), lista[1:]))

pl = list(filter(lambda x: x[0] == 'Polska', lista))
de = list(filter(lambda x: x[0] == 'Niemcy', lista))

with open('zamowienia_polska.csv', 'w') as f:
    for line in pl:
        f.write(";".join(line)+'\n')

with open('zamowienia_niemcy.csv', 'w') as f:
    for line in de:
        f.write(";".join(line)+'\n')