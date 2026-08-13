from math import sqrt, pi


# P01
def area(l, w):
    return l * w


# P04
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


# P05
def isPrime(n):
    if n == 0 or n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# P07
def triangle(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        return "Not possible"
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


# P08
def circle(r):
    return pi * (r**2)


# P09
def sum(r):
    s = 0
    for i in range(1, r + 1, 2):
        s += i

    return s


# P10
def fibo(n):
    if n <= 1:
        return n

    return fibo(n - 1) + fibo(n - 2)


# P13
def palindrome(s1, s2):
    a1 = list(s1)
    a2 = list(s2)

    if a1[::-1] == a2:
        return True
    else:
        return False
