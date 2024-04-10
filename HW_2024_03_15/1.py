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
is_valid_mail('abc.de@fghij')
#да


# Комментарий преподавателя:
# решение не вполне корректное.
# is_valid_mail('abc.de@fghij') будет считаться валидным адресом, но это не так.
# лучше всего было бы делить строку на две части по '@' и затем проверять вторую часть на '.'
# на пиши функцию с учетом этих исправлений
