def abs(x):
    if x < 0:
        return -x
    else:
        return x


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


def filter(function, iterable):
    result = []
    for element in iterable:
        if function(element):
            result.append(element)
    return result


def len(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count


def max(iterable):
    max_value = iterable[0]
    for element in iterable:
        if element > max_value:
            max_value = element
    return max_value


def min(iterable):
    min_value = iterable[0]
    for element in iterable:
        if element < min_value:
            min_value = element
    return min_value


def pow(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result


def round(number, n=0):
    x = str(number).split(".")

    [integer_part, decimal_part] = x
    decimal_part = decimal_part[: n + 1]

    return float(integer_part + "." + decimal_part)


def sum(iterable):
    total = 0
    for element in iterable:
        total += element
    return total
