with open('nums.txt', 'r') as f:
    number = '0'
    sum = 0
    for i in f.read():
        if i in '1234567890':
            number += i
        else:
            sum += int(number)
            number = '0'
    print(sum)
f.close()
