errors = [ '1004 ER_CANT_CREATE_FILE',
    '1005 ER_CANT_CREATE_TABLE',
    '1006 ER_CANT_CREATE_DB',
    '1007 ER_DB_CREATE_EXISTS',
    '1008 ER_DB_DROP_EXISTS',
    '1010 ER_DB_DROP_RMDIR',
    '1016 ER_CANT_OPEN_FILE',
    '1022 ER_DUP_KEY']
is_active = True
while is_active:
    x = input('Введите название ошибки: ')
    if x == '':
        is_active = False
        print('Вы вышли из программы')
    else:
        for i in range(len(errors)):
            error = errors[i]
            err = True
            if x == error[5:]:
                print(f'Номер ошибки: {error[0:5]}')
                err = False
                break
    if err:
        print('! value error !')

# Введите название ошибки: ER_CANT_OPEN_FILE
# Номер ошибки: 1016 
# Введите название ошибки: ER_GIPK_COLUMN_EXISTS
# ! value error !


# комментарий преподавателя:
# всё верно