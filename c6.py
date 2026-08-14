def gen(n):
    for i in range(1, n + 1, 2):
        yield i


for i in gen(100):
    print(i)
