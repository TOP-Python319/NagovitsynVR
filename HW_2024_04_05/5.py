with open('input.txt', 'r') as file:
    strings = file.readlines()
    with open('output.txt', 'w') as f:
        for i in range(len(strings)):
            print(f'{i+1}) {strings[i]}')
    f.close()
file.close()        
