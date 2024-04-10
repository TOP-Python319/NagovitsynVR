def Fibonacci(n:int):
    numbers = [1,1]
    for i in range(n):
        numbers.append(numbers[-1] + numbers[-2])
    return numbers

print(Fibonacci(17))
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]


# комментарий преподавателя:
# всё верно!