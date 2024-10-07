from random import choice

chars = ['你', '我', '是', '不', '的', '有', '他', '会', '什', '么', '在', '一', '这', '个', '些', '大', '小', '很', '没', '们', '但', '里', '那', '为', '人', '好', '她', '了', '中', '国', '上', '下', '横', '竖', '撇', '捺', '点', '提', '二', '三', '四', '五', '六', '七', '八', '九', '十', '百', '木', '火', '水', '土', '金', '口']

while True:
    length = int(input('Enter your desired length: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')