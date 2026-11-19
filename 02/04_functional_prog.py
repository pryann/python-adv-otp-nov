from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
# doubled_numbers = [i * 2 for i in numbers]
doubled_list = list(map(lambda x: x * 2, numbers))
print(type(doubled_list), doubled_list)


# even_list = [i for i in numbers if i % 2 == 0]
even_list = list(filter(lambda x: x % 2 == 0, numbers))
print(even_list)

multi = reduce(lambda x, y: x * y, numbers)
print(multi)
