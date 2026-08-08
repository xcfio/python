def even_gen():
    for i in range(2, 102, 2):
        yield i


for num in even_gen():
    print(num, end=" ")
