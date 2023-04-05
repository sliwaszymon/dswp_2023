# No ogólnie pliku zamówienia nie ma na tym repo, mam go bo robiłem laby z poprzedniego roku
# EDIT: ADRIAN DAŁ INFO ŻE PLIK ZARAZ BĘDZIE
import codecs
from datetime import datetime

lista = []
# zapis do listy
with codecs.open('zamowienia.csv', 'r', 'utf-8-sig') as f:
    for line in f:
        lista.append(line.replace('\n', '').replace('\r', '').replace(' z\x88', '').split(';'))

# zamiana przecinka na kropke
for line in lista[1:]:
    line[len(line)-1] = line[len(line)-1].replace(',','.').replace(' ', '')
    line[2] = datetime.strptime(line[2], '%d.%m.%Y').strftime('%Y-%m-%d')
    

pl = [x for x in lista if x[0] == 'Polska']
de = [x for x in lista if x[0] == 'Niemcy']

with open('zamowienia_polska.csv', 'w') as f:
    for line in pl:
        f.write(";".join(line)+'\n')

with open('zamowienia_niemcy.csv', 'w') as f:
    for line in de:
        f.write(";".join(line)+'\n')