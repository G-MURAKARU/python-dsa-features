from functools import cache


@cache
def climbing_stairs(steps: int):
    # climbing_stairs(n) = climbing_stairs(n-1) + climbing_stairs(n-2)
    # base case is when n <= 2
    if steps < 2:
        return 1
    return climbing_stairs(steps - 1) + climbing_stairs(steps - 2)


if __name__ == "__main__":
    print(climbing_stairs(3))
