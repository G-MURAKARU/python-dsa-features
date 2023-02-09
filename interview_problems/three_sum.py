def three_sum(
    numbers: list[int],
    target: int = 0,
) -> list[list[int]]:
    """
    three_sum finds all 3-digit combinations from numbers that add up to target

    Args:
        numbers (list[int]): a list of integers
        target (int, optional): target sum. Defaults to 0.

    Returns:
        list[list[int]]: list of 3-digit combinations adding up to target
    """

    # * three_sum = some_num + (two_sum) ( DP haha )

    # advantages of sorting the list beforehand:
    # 1. prevents duplicate solutions
    # 2. enables use of two-pointers two-sum solution
    numbers.sort()

    sols = []

    for index, value in enumerate(numbers):
        if index > 0 and value == numbers[index - 1]:
            continue

        new_target = target - value
        left_pointer = index + 1
        right_pointer = len(numbers) - 1
        # initialises at a new memory location, hence no clashes
        nums: list[list[int]] = []

        while left_pointer < right_pointer:
            left = numbers[left_pointer]
            right = numbers[right_pointer]

            if left + right == new_target:
                nums.append([value, left, right])
                right_pointer -= 1
                left_pointer += 1
            elif left + right > new_target:
                right_pointer -= 1
            else:
                left_pointer += 1

        sols.extend(nums)

    return sols


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4, 5]))
