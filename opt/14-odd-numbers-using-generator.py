def odd_gen():
    for i in range(1, 101, 2):
        yield i


for num in odd_gen():
    print(num, end=" ")
