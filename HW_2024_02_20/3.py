number = int(input('Введите число: '))
numbers = []

for i in range(1,number+1):
    if number % i==0:
        numbers.append(i)
print(sum(numbers))

# Введите число: 35
# 48

# Введите число: 50
# 93
