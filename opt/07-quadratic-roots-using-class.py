from math import sqrt


class QuadraticEquation:
    def __init__(self, a, b, c):
        d = b**2 - 4 * a * c

        if d < 0:
            print("Roots are not possible")

        elif d == 0:
            r = -b / (2 * a)
            print(f"One real root: {r}")

        else:
            x = (-b + sqrt(d)) / (2 * a)
            y = (-b - sqrt(d)) / (2 * a)
            print(f"Roots are {x} and {y}")


QuadraticEquation(1, -5, 6)
