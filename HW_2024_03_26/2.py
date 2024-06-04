def flatten(in_list):
    result = []
    for i in in_list:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([[1, 2, 3], [4, 5], [6]]))  
