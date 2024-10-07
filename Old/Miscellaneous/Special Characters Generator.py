from random import choice
 
chars = ['§', '¢', '£', '¤', '¥', '¦', '¨', '©', 'ª', '«', '¬', '®', 'ˉ', '°', '±', '²', '³', '´', 'µ', '¶', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', '÷']
 
while True:
    length = int(input('Enter your desired special character sentence length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')