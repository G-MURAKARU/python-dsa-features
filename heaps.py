import heapq
import random

data = [random.randint(1, 100) for _ in range(20)]

print(data)

heapq._heapify_max(data)

print(data)
