
x = float(input('Введите первое число: '))
if x < 0:
    x = 0
y = float(input('Введите второе число: '))
if y<0:
    y = 0
z = float(input('Введите третье число: '))
if z<0:
    z=0

out =x+y+z
formatted_out = "{:.2f}".format(out) 
print(f'Сумма положительных чисел равна: {formatted_out}')

