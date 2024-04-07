def is_valid_mail(mail: str):
    if '@' in mail:
        if '.' in mail:
            print('да')
        else:
            print('нет')
    else:
        print('нет')

is_valid_mail('sgd@ya.ru')
#да
is_valid_mail('abcde@fghij')
#нет
