import copy
import gc


def best_sum(target_sum: int, numbers: list[int], sum_cache: dict = None) -> list[int]:
    if sum_cache is None:
        sum_cache = {}

    # print(sum_cache)

    if target_sum in sum_cache:
        return copy.copy(sum_cache.get(target_sum))

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_combination: list[int] = None

    for num in numbers:
        new = target_sum - num

        # unbounded knapsack
        result = best_sum(new, numbers, sum_cache)

        if result is not None:
            # reached when target sum == 0
            result.append(num)
            if shortest_combination is None or len(result) < len(shortest_combination):
                shortest_combination = result

    sum_cache[target_sum] = copy.copy(shortest_combination)
    gc.collect()
    return shortest_combination


if __name__ == "__main__":
    print(best_sum(10, [2, 1, 3, 4]))
    # print(best_sum(3000, [19, 11, 5]))
