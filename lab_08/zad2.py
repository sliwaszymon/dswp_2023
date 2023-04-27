import datetime
import random
from array import array

# zapisanie tablicy do pliku oraz jej wczytanie
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
with open('floats_array.bin', 'wb') as file_arr:
    tab_save_start = datetime.datetime.now()
    tab_of_floats.tofile(file_arr)
    tab_save_stop = datetime.datetime.now()

# wczytujemy ponownie dane do tablicy floatów
tab_of_floats_loaded = array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_load_start = datetime.datetime.now()
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
tab_load_stop = datetime.datetime.now()
file_arr.close()


# i analogiczna operacja dla listy
list_of_floats = [random.random() for _ in range(1_000_000)]
with open('floats_list.txt', 'w') as file_arr:
    list_save_start = datetime.datetime.now()
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
    list_save_stop = datetime.datetime.now()

with open('floats_list.txt', 'r') as file_list:
    list_load_start = datetime.datetime.now()
    list_of_floats_loaded = file_list.readlines()
    list_load_stop = datetime.datetime.now()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
print(list_of_floats_loaded[:10])

tab_save = tab_save_stop - tab_save_start
tab_load = tab_load_stop - tab_load_start

list_save = list_save_stop - list_save_start
list_load = list_load_stop - list_load_start

print('tab save: ', tab_save, ' tab load: ', tab_load)
print('list save: ', list_save, ' list load: ', list_load)

# [0.6419814140749396, 0.5702882597453919, 0.7871604089132762, 0.27234578601190085, 0.956468479897134, 2.113575859741257e-05, 0.9267398642208258, 0.49364721971514347, 0.9870196093583469, 0.9749437632740158]
# tab save:  0:00:00.021184  tab load:  0:00:00
# list save:  0:00:09.856308  list load:  0:00:00.235056