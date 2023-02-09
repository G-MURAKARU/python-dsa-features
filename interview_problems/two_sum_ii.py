def two_sum(target: int, numbers: list[int]) -> list[int]:
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        if numbers[left_pointer] + numbers[right_pointer] == target:
            return [left_pointer + 1, right_pointer + 1]
        elif numbers[left_pointer] + numbers[right_pointer] > target:
            right_pointer -= 1
        else:
            left_pointer += 1


if __name__ == "__main__":
    target = 9
    numbers = [1, 3, 4, 5, 7, 10, 11]
    print(two_sum(target, numbers))
