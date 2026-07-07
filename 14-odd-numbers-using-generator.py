def odd_gen():
    for i in range(1, 101):
        if i % 2 != 0:
            yield i


for num in odd_gen():
    print(num, end=" ")
