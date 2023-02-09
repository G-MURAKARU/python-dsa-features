import contextlib
import copy


def all_construct(
    target: str, word_bank: list[str], memo: dict = None
) -> list[list[str]]:
    """
    all_construct returns all substrings from word_bank that can be concatenated to form target
    you can use each word bank word an infinite number of times - UNBOUNDED KNAPSACK PROBLEM

    Args:
        target (str): string to construct
        word_bank (list[str]): list of possible substrings

    Returns:
        list[list[str]]: list of substrings that construct target
    """

    # base case - empty target string (there is 1 way to create an empty string - take nothing from the word bank)
    if memo is None:
        memo = {}

    if not target:
        return [[]]

    if target in memo:
        return copy.copy(memo.get(target))

    all_ways = []

    # recursive loop
    for string in word_bank:
        with contextlib.suppress(ValueError):
            if target.index(string) == 0:
                suffix = target[len(string) :]
                suffix_ways = all_construct(suffix, word_bank, memo)
                target_ways = []
                for word in suffix_ways:
                    word.insert(0, string)
                    target_ways.append(word)
                all_ways.extend(
                    target_ways
                )  # if target_ways is an empty iterable, extend does nothing

    memo[target] = copy.copy(all_ways)
    return all_ways


if __name__ == "__main__":
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(all_construct(("e" * 40) + "f", ["e" * i for i in range(1, 6)]))
