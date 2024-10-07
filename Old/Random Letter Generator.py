from random import choice
 
chars = ['q ', 'w ', 'e ', 'r ', 't ', 'y ', 'u ', 'i ' , 'o ' , 'p ', 'a ', 's ', 'f ', 'g ', 'h ', 'j ', 'k ', 'l ', 'z ', 'x ', 'c ', 'v ', 'b ', 'n ', 'm ']
 
while True:
    length = int(input('26 Maximum | Enter your desired length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')