from zad3 import User
import random
import pickle

usernames = ['ziomek1', 'poziomek1', 'czekoladek', 'wariatek']
emails = ['ugabuga@gmail.com', 'wojnatotalna@wp.pl', 'pollitranadwoch@o2.pl', 'studentswiata@uwm.edu.pl']
addresses = ['Olsztyn', 'Kętrzyn', 'Mrągowo', 'Działdowo']

users = []
while len(usernames) > 0:
    temp_usr = User(usernames.pop(random.randint(0, len(usernames)-1)), \
                    emails.pop(random.randint(0, len(emails)-1)), \
                    addresses.pop(random.randint(0, len(addresses)-1)), \
                    str(random.randint(500000000, 999999999)))
    users.append(temp_usr)

print("ORIGINAL USERS")
for idx, user in enumerate(users):
    print(idx, user)

with open('user_list_instancja', 'wb') as f:
    pickle.dump(users, f)

with open('user_list_instancja', 'rb') as f:
    pickled_user_list = pickle.load(f)

print("PICKLED USERS")
for idx, pickled_user in enumerate(pickled_user_list):
    print(idx, pickled_user)