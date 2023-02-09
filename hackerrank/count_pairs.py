def countPairs(arr):
    # Write your code here
    # Write your code here
    from collections import Counter
    from itertools import combinations
    from math import log2

    my_counter = Counter(arr)
    my_set = set(arr)
    result = 0

    if len(my_set) == 1:
        ele = my_counter.get(arr[0])
        return (ele * (ele - 1)) / 2

    my_combs = combinations(my_set, 2)

    for comb in my_combs:
        first_bitwise_and = comb[0] & comb[0]
        if first_bitwise_and > 0:
            current_log = log2(first_bitwise_and)
            if current_log.is_integer():
                first = my_counter.get(comb[0])
                result += (first * (first - 1)) / 2

        second_bitwise_and = comb[1] & comb[1]
        if second_bitwise_and > 0:
            current_log = log2(second_bitwise_and)
            if current_log.is_integer():
                second = my_counter.get(comb[1])
                result += (second * (second - 1)) / 2
        third_bitwise_and = comb[0] & comb[1]
        if third_bitwise_and > 0:
            current_log = log2(third_bitwise_and)
            if current_log.is_integer():
                first = my_counter.get(comb[0])
                second = my_counter.get(comb[1])
                result += first * second

    return result


print(countPairs([5, 5, 5, 5, 5, 3, 3, 3]))
