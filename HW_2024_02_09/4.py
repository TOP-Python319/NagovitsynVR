cell1 = input('Введите координаты на первой доске: ')
cell2 = input('Введите координаты на второй доске: ')

def is_same_color(cell1, cell2):
    def is_black(cell):
        column, row = cell
        column_index = ord(column) - ord('a')
        row_index = int(row) - 1
        return (column_index + row_index) % 2 == 0

    return is_black(cell1) == is_black(cell2)

if is_same_color(cell1, cell2):
    print("да")
else:
    print("нет")

# Введите координаты на первой доске: a8
# Введите координаты на второй доске: d1
# да
    
# Введите координаты на первой доске: a7
# Введите координаты на второй доске: b7
# нет
