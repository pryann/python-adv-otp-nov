def generate_id():
    yield 1
    yield 2
    yield 3


id_generator = generate_id()
print(id_generator)
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
# StopIteration
# print(next(id_generator))

for i in generate_id():
    print(i)
