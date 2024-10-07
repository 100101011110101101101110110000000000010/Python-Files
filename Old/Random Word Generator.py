import random
from random import choice
 
chars = ['rice ', 'glass ', 'fast ', 'foamy ', 'calm ', 'agreeable ', 'error ', 'bead ', 'damp ', 'huge ', 'throat ', 'donkey ', 'sin ', 'cheese ', 'tired ', 'foolish ', 'wait ', 'hose ', 'plausible ', 'wrench ', 'momentous ', 'spooky ', 'breakable ', 'royal ', 'unnatural ', 'school ', 'fowl ', 'raspy ',
        'strap ', 'aquatic ', 'mouth ', 'daffy ', 'furry ', 'stone ', 'scrub ', 'needless ', 'downtown ', 'dirt ', 'object ', 'calm ', 'error ', 'tasty ', 'oranges ', 'telling ', 'long-term ', 'copper ', 'rich ', 'acoustic ', 'future ', 'incompetent ', 'jog ', 'wiggly ', 'weary ', 'march ', 'mate ',
        'recognise ', 'needy ', 'punch ', 'car ', 'crooked ', 'steady ', 'list ', 'silky ', 'sturdy ', 'hard-to-find ', 'language ', 'recess ', 'health ', 'angle ', 'obsolete ', 'lonely ', 'file ', 'psychedelic ', 'bit ', 'dogs ', 'festive ', 'position ', 'cagey ', 'friends ', 'check ', 'futuristic ',
        'giddy ', 'insect ', 'request ', 'thing ', 'dime ', 'cloistered ', 'tick ', 'ceaseless ', 'brick ', 'dad ', 'linen ', 'precede ', 'expansion ', 'zephyr ', 'air ', 'harmonious ', 'basketball ', 'uneven ', 'cherries ', 'mountainous ', 'nervous ', 'toad ', 'deafening ', 'license ', 'dapper ', 'blind ',
        'obtainable ', 'consist ', 'tank ', 'testy ', 'transport ', 'malicious ', 'awesome ', 'partner ', 'sweater ', 'wrist ', 'ear ', 'leather ', 'didactic ', 'shrug ', 'alarm ', 'irate ', 'station ', 'fail ', 'thinkable ', 'file ', 'chilly ', 'bewildered ', 'approval ', 'stove ', 'aware ', 'cable ',
        'sisters ', 'attract ', 'friction ', 'play ', 'perform ', 'synonymous ', 'murky ', 'form ', 'lamp ', 'conscious ', 'swanky ', 'astonishing ', 'lake ', 'necessary ', 'chicken ', 'simple ', 'juvenile ', 'alive ', 'stocking ', 'uncovered ', 'coal ', 'pretend ', 'glorious ', 'tendency ', 'tendency ',
        'tricky ', 'weak ', 'possible ', 'spectacular ', 'overwrought ', 'extra-small ', 'toys ', 'beef ', 'vegetable ', 'loss ', 'impossible ', 'haunt ', 'zoo ', 'heat ', 'exciting ', 'protective ', 'shaggy ', 'incredible ', 'courageous ', 'tank ', 'difficult ', 'wobble ', 'cause ', 'melt ', 'meaty ',
        'tip ', 'honorable ', 'nice ', 'harm ', 'thick ', 'afraid ', 'tenuous ', 'quartz ', 'unwritten ', 'live ', 'branch ', 'flag ', 'strange ', 'quicksand ', 'magnificent ', 'collect ', 'staking ', 'zany ', 'quill ', 'obedient ', 'suggestion ', 'trail ', 'funny ', 'middle ', 'employ ', 'wren ', 'bee ',
        'ocean ', 'whip ', 'hypothesize ', 'offer ', 'scrape ', 'tree ', 'long ', 'mayor ', 'breakfast ', 'worm ', 'drag ', 'day ', 'kneel ', 'nap ', 'snatch ', 'guideline ', 'miner ', 'ready ', 'separate ', 'stamp ', 'bend ', 'boat ', 'necklace ', 'liberty ', 'shoulder ', 'memory ', 'nice', 'year', 'stick ',
        'gold ', 'trouser ', 'hostage ', 'grant ', 'nationalist ', 'garlic ', 'lake ', 'worker ', 'suitcase ', 'fiction ', 'onion ', 'dismissal ', 'punish ', 'strain ', 'resident ', 'design ', 'rare ', 'applaud ', 'table ', 'dilute ', 'basketball ', 'adviser ', 'flag ', 'motorist ', 'view ', 'fact ', 'order ',
        'luxuriant ', 'awesome ', 'glamorous ']
random.shuffle(chars)
 
while True:
    length = int(input('Enter your desired amount of random words: '))
    password = []
    for i in range(length):
        password.append(choice(chars))
 
    print('\n' + ''.join(password) + '\n')



    #|, ''