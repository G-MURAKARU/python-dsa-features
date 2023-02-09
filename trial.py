# def even(number):
#     return number % 2 == 0


# a = [1, 2, 3, 4, 5]
# a.sort(key=even, reverse=True)
# print(a)

# import time
# from functools import cache, lru_cache


# @cache
# def fib(n):
#     return n if n < 2 else fib(n - 1) + fib(n - 2)


# def main():
#     start = time.perf_counter()

#     for i in range(1000):
#         print(i, fib(i))

#     end = time.perf_counter()

#     print(f"Time taken was {(end - start):.2f} seconds.")


# from typing import Any


# def flatten_list(input_list: list[Any], output_list: list[Any] = None):
#     """
#     flatten_list _summary_

#     Args:
#         input_list (list[Any]): _description_
#     """
#     if output_list is None:
#         output_list = []

#     for element in input_list:
#         if isinstance(element, list):
#             flatten_list(element, output_list=output_list)
#         else:
#             output_list.append(element)

#     return output_list


# if __name__ == "__main__":
#     print(
#         flatten_list(
#             input_list=[
#                 1,
#                 2,
#                 3,
#                 [
#                     4,
#                     5,
#                     [6, 7, 8, 9],
#                     10,
#                     11,
#                     [12, 13, 14, [15, 16], 17],
#                     18,
#                     19,
#                     [20, [21, 22]],
#                 ],
#                 23,
#             ]
#         )
#     )

# import itertools


# def probability(n, letters, k):
#     indices = {index for index, value in enumerate(letters, start=1) if value == "a"}

#     combination = itertools.combinations(range(1, n + 1), k)
#     found = 0
#     combs = 0
#     for comb in combination:
#         combs += 1
#         comb = set(comb)
#         found += 1 if indices.intersection(comb) else 0

#     return found / combs


# if __name__ == "__main__":
#     n = int(input().strip())

#     letters = input().split(" ")

#     k = int(input().strip())

#     print(n)
#     print(letters)
#     print(k)

#     print(probability(n, letters, k))


# from collections import deque


# def stack_cubes(cubes):
#     my_deque = deque(cubes)
#     current = float("inf")

#     while my_deque:
#         if all([my_deque[0] <= current, my_deque[-1] <= current]):
#             current = (
#                 my_deque.popleft() if my_deque[0] >= my_deque[-1] else my_deque.pop()
#             )
#             continue
#         return "No"

#     return "Yes"


# print(stack_cubes([4, 3, 2, 1, 3, 4]))

# edges: list[list[int]] = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
# graph: dict[str, list] = {}

# for edge in edges:
#     for node in edge:
#         if node in graph:
#             continue
#         graph[node]: list[str] = []
#         for _edge in edges:
#             if node in _edge:
#                 graph[node].append(_edge[_edge.index(node) - 1])

# print(graph)


# def _get_ways(n, c):
#     if n == 0:
#         return True

#     if n < 0:
#         return False

#     for coin in c:
#         new_change = n - coin
#         if _get_ways(new_change, c):
#             break

#     return True


# def getWays(n, c):
#     # Write your code here
#     ways = 0

#     for coin in c:
#         new = n - coin
#         if _get_ways(new, c):
#             ways += 1

#     return ways


# print(getWays(4, [1, 2, 3]))
# print(getWays(4, 1))


# from functools import cache


# @cache
# def fib(t1, t2, n):
#     if n <= 1:
#         return t1
#     return t2 if n == 2 else (fib(t1, t2, n - 1)) ** 2 + fib(t1, t2, n - 2)


# print(fib(2, 0, 12))

# n = 10

# nodes = [1] * (n + 1)

# cost = [0] * (n + 1)

# for i in range(1, len(nodes)):
#     nodes[i] = (nodes[i - 1] * 4) + 2

# import itertools

# k = [[1, 2], [4], [5, 6, 2], [1, 2], [3], [4]]
# k.sort()
# x = [k for k, _ in itertools.groupby(k)]
# print(x)


# def find_combinations(x, y):
#     combos = []
#     for i in range(1 << len(y)):
#         combo = [y[j] for j in range(len(y)) if (i & (1 << j)) > 0]
#         if sum(combo) == x:
#             combos.append(combo)

#     return len(combos)


# x = 100
# y = [7, 1, 2, 3, 4, 73, 45, 21, 19, 10, 20]
# print("Combinations of integers from", y, "that add up to", x, "are:")
# print(find_combinations(x, y))


# def combinations_sum(x, y):
#     count = 0
#     for i in range(len(y)):
#         if x == 0:
#             count += 1
#         elif x > 0:
#             count += combinations_sum(x - y[i], y)

#     return count


# # Driver program to test above function
# x = 5  # target sum
# y = [1, 2, 3]  # list of integers
# print("Number of combinations that sum to", x, "are", combinations_sum(x, y))


# def find_combos(x, y):
#     combos = []
#     for i in range(len(y)):
#         if x == y[i]:
#             combos.append([y[i]])
#         else:
#             for combo in combos:
#                 if sum(combo) + y[i] == x:
#                     combo.append(y[i])

#     return combos


# x = 5
# y = [1, 2, 3]
# print(find_combos(x, y))


def lonelyinteger(a):
    # Write your code here
    a.sort()
    for i in range(len(a) - 2):
        print(a[i])
        print(a[i + 1])
        if a[i] != a[i + 1]:
            return a[i]

    return a[-1]


print(lonelyinteger([0, 0, 1, 2, 1]))

# transpose of a matrix
# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

test_str = "Murakaru"

for i in range(len(test_str)):
    for j in range(i + 1, len(test_str) + 1):
        print(test_str[i:j])
