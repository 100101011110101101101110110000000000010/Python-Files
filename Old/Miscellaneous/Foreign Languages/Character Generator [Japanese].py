from random import choice

chars = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

while True:
    length = int(input('Enter your desired length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')