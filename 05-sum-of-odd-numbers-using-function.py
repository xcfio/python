def sum_odd():
    total = 0
    for i in range(1, 101, 2):
        total += i
    return total


print(sum_odd())
