from math import sqrt, pi


# P2
class QuadraticEquation:
    def __init__(self, a, b, c):
        d = b**2 - 4 * a * c

        if d > 0:
            x = (-b + sqrt(d)) / (2 * a)
            y = (-b - sqrt(d)) / (2 * a)
            print(f"Roots are real and they are {x} and {y}")

        elif d == 0:
            x = -b / (2 * a)
            print(f"Root is {x}")

        else:
            print("Not possible")


# P3
class Triangle:
    def __init__(self, a, b, c):
        s = (a + b + c) / 2
        a = sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Area is {a}")


# P4
class Max:
    def __init__(self, a, b, c):
        if a > b and a > c:
            print(f"Max: {a}")
        elif b > a and b > c:
            print(f"Max: {b}")
        else:
            print(f"Max: {c}")


# P5
class Circle:
    def __init__(self, r):
        a = pi * (r**2)
        print(f"Area is {a}")
