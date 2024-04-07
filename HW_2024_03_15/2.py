fruits = []
is_active = True

while is_active:
    x = input('Введите название фрукта для списка: ')
    if x == '':
        is_active = False
    else:
        fruits.append(x)

out = ''
for i in range(len(fruits)):
    if i == 0:
        out += fruits[i]
    elif i < len(fruits) - 1:
        out += ', ' + fruits[i]
    elif i < len(fruits):
        out += ' и ' + fruits[i]
print(out)

# Введите название фрукта для списка: апельсин
# Введите название фрукта для списка: яблоко
# Введите название фрукта для списка: груша 
# Введите название фрукта для списка: 
# апельсин, яблоко и груша 
