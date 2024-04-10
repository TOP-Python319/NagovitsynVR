def counter(n):
    count = 0
    if n == 1:
        count = 4
    elif n > 1:
        last_number = int('9'*n)
        first_number = int('1'*n) - int('1'*(n-1))
        
        for i in range(first_number,last_number+1):
            if i % 2 > 0 and i % 3 > 0 and i % 5>0 and i % 7>0:
                count += 1
    return count
            
    

print(counter(1))
print(counter(3))

# 4
# 206


# комментарий преподавателя:
# всё верно