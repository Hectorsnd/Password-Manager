from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()

    return key


Master_Password = input('Type your password: ')

key = load_key() + Master_Password.encode
fer = Fernet(key)

def view():

    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print('User: ', user, ', Passaword: ', fer.decrypt(passw.encode()).decode)

def add():

    name = input('Account name: ')
    pwd = input('Password: ')

    with open('Password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input('Would you like to add a new password or view existing ones, to quit press q (add/view)?: ').lower()

    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid option')
        continue