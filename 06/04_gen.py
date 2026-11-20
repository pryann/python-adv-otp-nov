def square_input():
    while True:
        num = yield
        yield num**2


gen = square_input()
next(gen)
print(gen.send(10))
next(gen)
print(gen.send(13))
