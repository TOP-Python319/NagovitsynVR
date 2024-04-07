scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = input('Введите слово: ').upper()
word = list(word.replace('Ё', 'Е'))
scores = 0

for x in word:
    if x in scores_letters[1]:
        scores += 1
    elif x in scores_letters[2]:
        scores += 2
    elif x in scores_letters[3]:
        scores += 3
    elif x in scores_letters[4]:
        scores += 4
    elif x in scores_letters[5]:
        scores += 5
    elif x in scores_letters[8]:
        scores += 8
    elif x in scores_letters[10]:
        scores += 10
    elif x in scores_letters[15]:
        scores += 15

print(scores)
    
# Введите слово: синхрофазотрон
# 29           
        
