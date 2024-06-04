with open('data.txt', 'r') as f:
    strings = f.readlines()
    reversed = strings[::-1]
    print(strings)
    for i in range(len(reversed)):
        print(f'{reversed[i]} \n')
f.close()
