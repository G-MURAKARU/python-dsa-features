def partition(target_sum: int, numbers: list[int]) -> bool:
    if target_sum % 2:
        return False

    target_sum //= 2

    def helper_func(target: int, numbers: list[int], index: int) -> bool:
        new_target = target - numbers[index]
        if new_target == 0:
            return True
        if new_target < 0:
            return False

        return helper_func(new_target, numbers, index + 1) or helper_func(
            target, numbers, index + 1
        )

    return helper_func(target_sum, numbers, 0)


print(partition(22, [1, 5, 11, 5]))
