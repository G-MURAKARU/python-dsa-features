from collections import Counter
from itertools import combinations
from string import digits

ints = map(int, digits[1:])
combs = combinations(ints, 3)
my_list: list[list[int]] = [list(comb) for comb in combs if sum(comb) == 15]

flattened_list = []
for element in my_list:
    flattened_list.extend(element)

my_counter = Counter(flattened_list)
centre, edges, vertices = 0, [], []
for item in my_counter:
    if my_counter[item] == 4:
        centre = item
    elif my_counter[item] == 3:
        vertices.append(item)
    else:
        edges.append(item)


def sth(sth_else):
    return [list(x) for x in combinations(sth_else, 2) if sum(x) == 10]


diags = sth(vertices)
sides = sth(edges)

print("centre:", centre)
print("vertices:", diags)
print("edges:", sides)
