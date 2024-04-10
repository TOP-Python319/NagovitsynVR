numbers = []
is_valid = True
while is_valid:
    x = int(input('Введите число, кратное семи: '))
    
    if x % 7 == 0:
        numbers.append(x)
        is_valid = True
        
    else:
        is_valid = False
        
sorted_num = sorted(numbers, reverse = True)
print(sorted_num)

# Введите число, кратное семи: 35
# Введите число, кратное семи: 35
# Введите число, кратное семи: 21 
# Введите число, кратное семи: 7
# Введите число, кратное семи: 1
# [35, 35, 21, 7]


# комментарий преподавателя:
# всё верно!
