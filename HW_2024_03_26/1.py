def double_factorial(number:int) -> int:
    if number <2:
        return 1
    return number * double_factorial(number - 2)

print(double_factorial(6))
print(double_factorial(5))
print(double_factorial(2))

# 48
# 15
# 2
