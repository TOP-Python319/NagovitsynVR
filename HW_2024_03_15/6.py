def is_binary(number:str):
    num = set(number)
    binary_set = {'0','1','b'}
    if num <= binary_set:
        print('да')
    else:
        print('нет')

is_binary('b1100')
is_binary('1100')
is_binary('0b010102')

# да
# да
# нет
