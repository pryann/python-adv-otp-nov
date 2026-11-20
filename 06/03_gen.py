def generate_id(start, inc):
    id_num = start + inc
    while True:
        yield id_num
        id_num += inc


ids = generate_id(10, 10)
print(next(ids))
print(next(ids))
print(next(ids))

for i in ids:
    print(i)
    if i > 10_000:
        # break
        ids.close()

# print(next(ids))
