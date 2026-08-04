def num(x):
    for i in range(x):
        yield i


for i in num(29):
    print(i)
