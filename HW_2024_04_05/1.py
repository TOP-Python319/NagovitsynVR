f = open('text.txt', 'r')
data = f.readline()
reversed_data = []
n = 1
for i in range(len(data)):
    reversed_data.append(data[-n])
    n += 1
print(reversed_data)

f.close()

# ['.', 'e', 'n', 'i', 'l', ' ', 'h', 'c', 'a', 'e', ' ', 'f', 'o', ' ', 'r', 'e', 't', 't', 'e', 'l', ' ', 't', 's', 'r', 'i', 'f', ' ', 'e', 'h', 't', ' ', 't', 'u', 'o', ' ', 't', 'n', 'i', 'r', 'p', ' ', 'd', 'n', 'a', ' ', 't', 'x', 't', '.', 'e', 'g', 'a', 's', 's', 'e', 'm', '_', 't', 'e', 'r', 'c', 'e', 's', ' ', 'd', 'a', 'e', 'R']
