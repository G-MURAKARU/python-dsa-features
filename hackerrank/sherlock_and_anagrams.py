from collections import defaultdict
from itertools import combinations


def sherlock_and_anagrams(string: str) -> int:
    substrings_dict: dict = defaultdict(list)

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring: str = "".join(sorted(string[i:j]))
            substrings_dict[substring].append(substring)

    anagrams = sum(
        len(list(combinations(item, 2))) for item in substrings_dict.values()
    )

    print(anagrams)


sherlock_and_anagrams("abcd")
