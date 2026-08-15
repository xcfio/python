def fibo(n):
    l = []

    a, b = 0, 1
    for _ in range(n + 1):
        l.append(a)
        a, b = b, a + b

    return l
