# def increase_by_one(num):
#     return num + 1

increase_by_one = lambda num: num + 1

print(increase_by_one(10))
print(increase_by_one(133))


def make_incrementor(n):
    return lambda x: x + n


f_42 = make_incrementor(10)
print(f_42(10))
print(f_42(100))


def apply(numbers, fn):
    # result = []
    # for number in numbers:
    #     result.append(fn(number))
    # return result
    return [fn(i) for i in numbers]


print(apply([1, 2, 3, 4, 5], lambda x: x * 2))
