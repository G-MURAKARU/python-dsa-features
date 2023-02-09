def two_sum(target: int, numbers: list[int]) -> list[int]:
    hash_map = {}

    for index, value in enumerate(numbers):
        diff = target - value
        if diff in hash_map:
            return [hash_map.get(diff), index]

        hash_map[value] = index


if __name__ == "__main__":
    target = 4
    numbers = [2, 1, 5, 3]
    print(two_sum(target, numbers))
