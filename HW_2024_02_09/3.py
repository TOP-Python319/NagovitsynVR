year_from_user = int(input('Введите год: '))

if year_from_user % 400 == 0:
    print('Високосный')
elif year_from_user % 100 == 0:
    print('Обычный')
elif year_from_user % 4 == 0:
    print('Високосный')
else:
    print('Обычный')