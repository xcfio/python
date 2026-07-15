# 01 - String Concatenation
def concat(x, y):
    return x + y


# 02 - Math Power
def pow(n, p):
    return n**p


# 03 - Math Square Root
def sqrt(n):
    return n**0.5


# 04 - Math PI
def pi():
    return 3.141592653589793


# 05 - Math Absolute Value
def abs(x):
    if x < 0:
        return -x
    else:
        return x


# 06 - Math Floor
def floor(x):
    if x < 0:
        return int(x) - 1
    else:
        return int(x)


# 07 - Math Ceiling
def ceil(x):
    if x < 0:
        return int(x)
    else:
        return int(x) + 1


# 08 - Iterable Sum
def sum(x):
    t = 0
    for i in x:
        t += i
    return t


# 09 - Iterable All
def all(x):
    for i in x:
        if not i:
            return False
    return True


# 10 - Iterable Any
def any(x):
    for i in x:
        if i:
            return True
    return False


# 11 - Iterable Len
def len(x):
    c = 0
    for _ in x:
        c += 1
    return c


# 12 - Iterable Max
def max(x):
    m = x[0]
    for i in x:
        if i > m:
            m = i
    return m


# 13 - Iterable Min
def min(x):
    m = x[0]
    for i in x:
        if i < m:
            m = i
    return m


# 14 - Iterable Reverse
def reverse(x):
    return x[::-1]
