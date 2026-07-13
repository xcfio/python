from typing import Iterable, Any


# 01 - String Concatenation
def concat(s1: str, s2: str) -> str:
    return s1 + s2


# 02 - Math Power
def pow(num: float, pow: float) -> float:
    return num**pow


# 03 - Math Square Root
def sqrt(num: float) -> float:
    return num**0.5


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


# 08 - Number Round
def round(num: float, n: int = 0) -> float:
    x = str(num).split(".")

    [i, d] = x
    d = d[: n + 1]

    return float(i + "." + d)


# 09 - Iterable Sum
def sum(it: Iterable[float]) -> float:
    t: float = 0
    for i in it:
        t += i
    return t


# 10 - Iterable All
def all(it: Iterable) -> bool:
    for i in it:
        if not i:
            return False
    return True


# 11 - Iterable Any
def any(it: Iterable) -> bool:
    for i in it:
        if i:
            return True
    return False


# 12 - Iterable Len
def len(it: Iterable) -> int:
    c = 0
    for _ in it:
        c += 1
    return c


# 13 - Iterable Max
def max(it: list) -> Any:
    m = it[0]
    for i in it:
        if i > m:
            m = i
    return m


# 14 - Iterable Min
def min(it: list) -> Any:
    m = it[0]
    for i in it:
        if i < m:
            m = i
    return m
