# def power_sum(target: int, power: int) -> int:
#     powers = []
#     base = 1

#     while (number := base**power) <= target:
#         powers.append(number)
#         base += 1
#     sums = [0]

#     # for index in range(len(powers) - 1, -1, -1):
#     #     new_values = [found_sum + powers[index] for found_sum in sums]
#     #     sums.extend(new_values)

#     # return sums.count(target)

#     count = 0

#     for index in range(len(powers) - 1, -1, -1):
#         new_values = []
#         for found_sum in sums:
#             if (new_sum := found_sum + powers[index]) == target:
#                 count += 1
#             new_values.append(new_sum)
#         sums.extend(new_values)

#     return count


# print(power_sum(200, 2))


def power_sum(X: int, N: int) -> int:
    def helper_func(target: int, power: int, number: int) -> int:
        new_target = target - (number**power)
        if new_target == 0:
            return 1
        if new_target < 0:
            return 0
        return helper_func(new_target, power, number + 1) + helper_func(
            target, power, number + 1
        )  # PICKING AND NOT PICKING !!!

    return helper_func(X, N, 1)


print(power_sum(800, 2))
