def create_counter():
    count = 0
    def increment(value=1):
        nonlocal count
        count += value
        return count
    
    def decrement(value=1):
        nonlocal count
        count -= value
        return count
    return increment, decrement

inc_1, dec_1 = create_counter()

print(inc_1())
print(inc_1(2))  
print(inc_1(3))  
print(inc_1(4))  
print(dec_1())  
print(dec_1(2))  

# 1
# 3
# 6
# 10
# 9
# 7
