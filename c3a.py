from c3b import fibo

n = int(input("Enter a num: "))
for i in range(n + 1):
    print(fibo(i), end=" ")
