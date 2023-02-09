from functools import cache


# @cache
def can_sum(target_sum: int, numbers: list[int], sum_cache: dict = None) -> bool:
    if sum_cache is None:
        sum_cache = {}

    print(sum_cache)

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    if target_sum in sum_cache:
        return sum_cache.get(target_sum)

    for num in numbers:
        new = target_sum - num
        if result := can_sum(new, numbers, sum_cache):
            sum_cache[target_sum] = result
            return True

    sum_cache[target_sum] = False
    return False


if __name__ == "__main__":
    print(can_sum(300, [7, 14]))
