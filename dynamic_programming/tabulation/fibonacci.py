def fibonacci(nth_value):
    if nth_value <= 0:
        return 0

    if nth_value <= 2:
        return nth_value - 1

    fibs = [0] * (nth_value + 1)
    fibs[1] = 1

    for n in range(2, len(fibs)):
        fibs[n] = fibs[n - 1] + fibs[n - 2]

    return fibs[-1]


# print(fibonacci(20500))
print(fibonacci(6))
