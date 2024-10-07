from random import choice
 
chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e', 'c', 'f', 'd', 'b', 'c']
 
while True:
    length = int(input('Enter your desired key length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')