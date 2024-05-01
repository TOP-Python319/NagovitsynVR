def orth_triangle(*, first_cathenus:float, second_cathenus:float=0, hypotenuse:float=0):
    # если введено все три значения
    if second_cathenus != 0 and hypotenuse != 0:
        return None
    # если введены невалидные значения
    if first_cathenus <= 0 and second_cathenus <= 0 and hypotenuse <= 0:
        return None
    # поиск гипотенузы
    if hypotenuse == 0:
        hypotenuse = (first_cathenus**2 + second_cathenus**2)**0.5
    # поиск катета
    if second_cathenus == 0:
        second_cathenus = (hypotenuse**2 - first_cathenus**2)**0.5
    # если все верно - вывод
    if first_cathenus<hypotenuse and second_cathenus<hypotenuse:
        return first_cathenus, int(second_cathenus), hypotenuse

print(orth_triangle(first_cathenus=5,hypotenuse=13))
print(orth_triangle(first_cathenus=3, hypotenuse=5))

# (5, 12, 13)
# (3, 4, 5)
