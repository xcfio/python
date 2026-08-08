from math import pi


def circle_area(r):
    return pi * (r**2)


r = float(input("Radius: "))
print(circle_area(r))
