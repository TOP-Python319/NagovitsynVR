first_coordinate = input('Введите начальную координату ладьи: ')
second_coordinate = input('Введите конечную координату ладьи: ')

def is_valid_move(first_coordinate, second_coordinate):
    if first_coordinate[0] == second_coordinate[0] or first_coordinate[1] == second_coordinate[1]:
        return "да"
    else:
        return "нет"

print(is_valid_move(first_coordinate, second_coordinate))

# Введите начальную координату ладьи: f1
# Введите конечную координату ладьи: e2
# нет

# Введите начальную координату ладьи: f1
# Введите конечную координату ладьи: g1
# да


# комментарий преподавателя:
# все верно, можно продолжать! =)