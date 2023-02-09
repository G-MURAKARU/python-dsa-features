# def find_first_last_index(input_array: list[int], target: int):
#     """
#     find_first_last_index finds the first and last occurrence of an element in a sorted array

#     Args:
#         input_array (list[int]): input sorted array of integers
#         target (int): element to find in array

#     Returns:
#         list: indices of first and last occurrences of target element
#     """
#     try:
#         return [
#             input_array.index(target),
#             max(idx for idx, val in enumerate(input_array) if val == target),
#         ]
#     except ValueError:
#         return [-1, -1]


def find_first(input_array: list[int], target: int):
    """
    find_first finds the first occurrence of an element in a sorted array using binary search

    Args:
        input_array (list[int]): input sorted array of integers
        target (int): element to find in array

    Returns:
        int: index of first occurrence of target element
    """

    if input_array[0] == target:
        return 0

    low: int = 0
    high: int = len(input_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if input_array[mid] == target and input_array[mid - 1] < target:
            return mid
        elif input_array[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def find_last(input_array: list[int], target: int):
    """
    find_last finds the last occurrence of an element in a sorted array using binary search

    Args:
        input_array (list[int]): input sorted array of integers
        target (int): element to find in array

    Returns:
        int: index of last occurrence of target element
    """

    if input_array[-1] == target:
        return len(input_array) - 1

    low: int = 0
    high: int = len(input_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if input_array[mid] == target and input_array[mid + 1] > target:
            return mid
        elif input_array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def find_first_last(input_array: list[int], target: int):
    """
    find_first_last finds the first and last occurrence of an element in a sorted array

    Args:
        input_array (list[int]): input sorted array of integers
        target (int): element to find in array

    Returns:
        list: indices of first and last occurrences of target element
    """

    if not input_array or input_array[0] > target or input_array[-1] < target:
        return [-1, -1]

    first: int = find_first(input_array, target)
    last: int = find_last(input_array, target)

    return [first, last]


from itertools import repeat
from random import choice, randint

my_array = []

for _ in range(20):
    repeater = repeat(randint(1, 100), randint(1, 10))
    my_array.extend(repeater)

my_array.sort()
print(my_array)

select = choice([0, 1])
target = choice(my_array) if select == 1 else 101
print(target)
print(find_first_last(my_array, target))
