first_coordinate = input('Введите начальную координату короля: ')
second_coordinate = input('Введите конечную координату короля: ')

def is_valid_move(first_coordinate, second_coordinate):

    first_y = int(first_coordinate[1])
    second_y = int(second_coordinate[1])
    first_letter = ord(first_coordinate[0]) 
    second_letter = ord(second_coordinate[0])  
    if first_y - second_y > 1 or first_letter - second_letter > 1 or second_letter - first_letter > 1 or second_y - first_y > 1:
        return "нет"
    return "да"
    
print(is_valid_move(first_coordinate, second_coordinate))

# Введите начальную координату короля: a1
# Введите конечную координату короля: a7
# нет

# Введите начальную координату короля: a1
# Введите конечную координату короля: a2
# да
