import contextlib


def can_construct(
    target: str, word_bank: list[str], substring_cache: dict = None
) -> bool:
    # brute force complexities:

    # time complexity: O(n^m * m) where n = len(word_bank) - # of nodes per tree level and
    # m = len(target) - height of tree
    # the second one is from the slicing operation

    # space complexity: O(m * m) = O(m^2)

    if substring_cache is None:
        substring_cache = {}

    if not target:
        return True

    if target in substring_cache:
        return substring_cache.get(target)

    # hint: substring must be a prefix of target string
    for word in word_bank:
        with contextlib.suppress(ValueError):
            if target.index(word) == 0:
                new_string = target[len(word) :]
                if can_construct(new_string, word_bank, substring_cache):
                    substring_cache[target] = True
                    print(substring_cache)
                    return True

    print(substring_cache)
    substring_cache[target] = False
    return False


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(can_construct(("e" * 40) + "f", ["e" * i for i in range(1, 6)]))

    # print((("e" * 40) + "f", ["e" * i for i in range(1, 6)]))
