def numbers_strip(numbers:list[float],quantity_to_delete:int=1, *, copy = False) -> list[float]:
    if copy:
        return numbers.copy()
    else:
        for i in range(quantity_to_delete):
            min_of_list = min(numbers)
            max_of_list = max(numbers)
            numbers.remove(min_of_list)
            numbers.remove(max_of_list)
        return numbers
    
sample = [1,2,3,4]
sample_stripped = numbers_strip(sample)
print(sample_stripped)

sample = [10,20,30,40,50]
sample_stripped = numbers_strip(sample,2,copy=True)
print(sample_stripped)

sample = [10,20,30,40,50]
sample_stripped = numbers_strip(sample,2,copy=False)
print(sample_stripped)

# [2, 3]
# [10, 20, 30, 40, 50]
# [30]
