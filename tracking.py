import getpass
import time
from itertools import product

pass_length = 4
correctpass = getpass.getpass(prompt='Input your pass(' + str(pass_length) + 'digits)：')
chars = '0123456789abcdefghijklmnopqrstuvwxyz'

if (len(correctpass) != pass_length):
    print('The password should have the specified number of digits.')
    exit()

def conf(text, repeat):
    passwords = product(text, repeat=repeat)
    for i, password in enumerate(passwords):
        print('\033[32m' + str(i) + ':' + ''.join(password) + '\033[0m')
        if ''.join(password) == correctpass:
            return ''.join(password)

def y_or_no():
    while True:
        choice = input('Do you want to start cracking your password?[y/N]：').lower()
        if choice == 'y':
            return True
        else:
            return False
if y_or_no():
    start = time.time()
    pw = conf(chars, pass_length)
    
    if pw is None:
        print('failure')
        pass
    else:
        print('Have identified the password.-->', pw)
    goal = time.time() - start
    print(goal, 'sec')
else:
    print('end.')