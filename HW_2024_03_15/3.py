
def is_part(first:list, second:list):
    for i in range(1 + len(first) - len(second)):
        if first[i:i+len(second)] == second:
            return 'да'
    return 'нет'
print(is_part([1,2,3,4],[1,2]))
#да

print(is_part([1,2,3,4],[2,4]))
#нет
