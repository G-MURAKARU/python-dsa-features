def find_maximum_subarray(numbers: list[int]) -> int:
    # Kadane's algorithm (or some version of it)
    max_sum: int = numbers[0]
    current_sum: int = 0

    for number in numbers:
        current_sum += number
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum


print(find_maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
