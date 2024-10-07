from random import choice
 
chars = ['🍎', '⚒️', '💀', '❗', '⛏️', '⚠️', '❕', '🔒', '🕒', '🤔', '😭', '😀', '😃',  '😄',  '😁',  '😆',  '😅',  '🤣',  '😂',  '🙂',  '🙃',  '🫠',  '😉',  '😊',  '😇',  '🥰']
 
while True:
    length = int(input('Enter your desired password length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')