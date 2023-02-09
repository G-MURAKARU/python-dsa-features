import copy


def how_sum(target_sum: int, numbers: list[int], sum_cache: dict = None) -> list[int]:
    if sum_cache is None:
        sum_cache = {}

    print(sum_cache)

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    if target_sum in sum_cache:
        return sum_cache.get(target_sum)

    for num in numbers:
        new = target_sum - num

        # 0/1 knapsack
        new_list: list[int] = copy.copy(numbers)
        new_list.pop(new_list.index(num))
        result = how_sum(new, new_list, sum_cache)

        # unbounded knapsack
        # result = how_sum(new, numbers, sum_cache)

        if result is not None:
            result.append(num)
            cached_result: list[int] = copy.copy(result)
            sum_cache[target_sum] = cached_result
            return result

    sum_cache[target_sum] = None
    return None


if __name__ == "__main__":
    print(how_sum(10, [3, 1, 5, 2, 4]))
    # print(how_sum(8, [5, 3, 2]))
    # print(how_sum(300, [7, 14]))
