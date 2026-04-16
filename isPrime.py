def isPrime(x):
    if x == 0 or x == 1:
        return False

    if x % 2 == 0:
        return False

    for i in range(3, int(x / 2), 2):
        if x % i == 0:
            return False

    return True


num = int(input("Enter a num: "))
print(isPrime(num))
