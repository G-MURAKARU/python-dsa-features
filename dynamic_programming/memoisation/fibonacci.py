from functools import cache


# @cache
def fibonacci(nth_term: int, fib_cache: dict = None) -> int:
    """
    fibonacci finds the nth term in the fibonacci sequence

    Args:
        nth_term (int): nth fibonacci term

    Returns:
        int: value of nth fibonacci term
    """

    # ! classic fib time complexity - 2^nth_term
    # * memoised fib time complexity - nth_term
    # * classic fib space complexity - nth_term

    if fib_cache is None:
        fib_cache = {}

    # print(fib_cache)

    # recursion base case, when nth term is 1 or 0
    if nth_term <= 2:
        return 1

    # memoisation FTW!
    if nth_term in fib_cache:
        return fib_cache.get(nth_term)

    # nth term is found by sum of previous 2 terms
    result: int = fibonacci(nth_term - 1, fib_cache) + fibonacci(
        nth_term - 2, fib_cache
    )

    # caching the result
    fib_cache[nth_term] = result

    # recursive call
    return result


if __name__ == "__main__":
    print(fibonacci(1000))

# compute fibonacci with memoisation in python
