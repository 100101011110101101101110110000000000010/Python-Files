from random import choice
 
chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
 
while True:
    length = int(input('Enter your desired error code length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')