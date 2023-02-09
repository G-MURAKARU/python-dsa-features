import time
from itertools import combinations

test_str = "Murakaru"

# Get all substrings of string
# Using list comprehension + string slicing
start = time.perf_counter()
res = [
    test_str[i:j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)
]
end = time.perf_counter()

print(f"time taken: {end-start}")

# Get all substrings of string
# Using itertools.combinations()
start = time.perf_counter()
res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r=2)]
end = time.perf_counter()

print(f"time taken: {end-start}")
