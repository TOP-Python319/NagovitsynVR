def countable_nouns(number:int, nouns:tuple) -> str:
    str_number = str(number)
    if number>10:
        if str_number[-1] == '1' and str_number[-2] != '1':
            print (f'{number} {nouns[0]}')
        elif str_number[-2] == '1':
            print(f'{number} {nouns[2]}')
    if number <= 10:
        if str_number[-1] == '1':
            print(f'{number} {nouns[0]}')
        elif str_number[-1] == '2' or str_number[-1] == '3' or str_number[-1] == '4':
            print(f'{number} {nouns[1]}')
        else:
            print(f'{number} {nouns[2]}')

countable_nouns(21, ('год', 'года', 'лет')) # 21 год
countable_nouns(11, ('год', 'года', 'лет')) # 11 лет
countable_nouns(2, ("год", "года", "лет")) # 2 года
countable_nouns(10, ("год", "года", "лет")) # 10 лет
countable_nouns(5, ("год", "года", "лет")) # 5 лет
