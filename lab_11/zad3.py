import pickle

class User:
    username: str
    email: str
    address: str
    tel: str

    def __init__(self, username, email, address, tel):
        self.username = username
        self.email = email
        self.address = address
        self.tel = tel
    
    def __str__(self):
        return '{ username: ' + self.username + ', email: ' + self.email + \
            ', address: ' + self.address + ', tel: ' + self.tel + ' }'
    

    def __repr__(self):
        return f'User(username: {self.username}, email: {self.email}, address: {self.address}, tel: {self.tel})'


if __name__ == "__main__":
    user = User("szymon", "szymon@wp.pl", "Olsztyn", "456321890")
    print("USER: ", user)

    with open('user_instancja', 'wb') as f:
        pickle.dump(user, f)

    with open('user_instancja', 'rb') as f:
        pickled_user = pickle.load(f)

    print("PICKLED USER: ", pickled_user)