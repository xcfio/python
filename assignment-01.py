from typing import Iterable, Any


# 01 - String Concatenation
def concat(x: str, y: str) -> str:
    return x + y


# 02 - Math Power
def pow(n: float, p: float) -> float:
    return n**p


# 03 - Math Square Root
def sqrt(n: float) -> float:
    return n**0.5


# 04 - Math PI
def pi() -> float:
    return 3.141592653589793


# 05 - Math Absolute Value
def abs(x: float) -> float:
    if x < 0:
        return -x
    else:
        return x


# 06 - Math Floor
def floor(x: float) -> int:
    if x < 0:
        return int(x) - 1
    else:
        return int(x)


# 07 - Math Ceiling
def ceil(x: float) -> int:
    if x < 0:
        return int(x)
    else:
        return int(x) + 1


# 08 - Iterable Sum
def sum(x: Iterable[float]) -> float:
    t: float = 0
    for i in x:
        t += i
    return t


# 09 - Iterable All
def all(x: Iterable) -> bool:
    for i in x:
        if not i:
            return False
    return True


# 10 - Iterable Any
def any(x: Iterable) -> bool:
    for i in x:
        if i:
            return True
    return False


# 11 - Iterable Len
def len(x: Iterable) -> int:
    c = 0
    for _ in x:
        c += 1
    return c


# 12 - Iterable Max
def max(x: list) -> Any:
    m = x[0]
    for i in x:
        if i > m:
            m = i
    return m


# 13 - Iterable Min
def min(x: list) -> Any:
    m = x[0]
    for i in x:
        if i < m:
            m = i
    return m


# 14 - Iterable Reverse
def reverse(x: list) -> list:
    return x[::-1]
