from random import choice
 
chars = ['0', '1']
 
while True:
    length = int(input('Enter your desired binary length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')