def unbounded_knapsack(target: int, numbers: list[int]) -> int:
    """
    unbounded_knapsack returns the sum of integers in numbers nearest to without exceeding the target value

    Args:
        target (int): sum limit
        numbers (list[int]): list of integers to sum to <= target

    Returns:
        int: sum closest to (without exceeding) target
    """

    # Write your code here
    if numbers.count(1) > 0:
        return target

    numbers.sort()

    # base case - when target == 0
    if target == 0:
        return 0

    num_numbers = len(numbers)

    if num_numbers == 0:
        return 0

    # recursive helper function
    def helper_func(limit: int, index: int, closest_sum: int = 0):
        if index == num_numbers:
            return 0

        new_limit: int = limit - numbers[index]

        if new_limit == 0:
            return numbers[index]

        if new_limit < 0:
            return 0

        current_sum = max(
            (numbers[index] + helper_func(new_limit, index, closest_sum)),
            helper_func(limit, index + 1, closest_sum),
        )

        closest_sum = max(closest_sum, current_sum)
        return closest_sum

    return helper_func(target, 0)


if __name__ == "__main__":
    print(unbounded_knapsack(2000, [1]))
