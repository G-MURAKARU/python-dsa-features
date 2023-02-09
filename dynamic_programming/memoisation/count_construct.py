import contextlib


def count_construct(
    target: str, word_bank: list[str], substring_cache: dict = None
) -> int:
    """
    count_construct counts the number of ways in which the target string can be constructed from concatenating words/substrings given in the word bank
    you can use each word bank word an infinite number of times - UNBOUNDED KNAPSACK PROBLEM

    Args:
        target (str): the string to be constructed
        word_bank (list[str]): list of possible substrings

    Returns:
        int: number of ways that target can be constructed
    """

    # initialise the cache for memoised solution
    if substring_cache is None:
        substring_cache = {}

    # search cache for previously counted substring
    if target in substring_cache:
        return substring_cache.get(target)

    # initialise a count variable to keep track of number of ways
    count = 0

    # the base case - if target becomes an empty string
    if not target:
        return 1

    # recursive logic - loop through each substring in word bank
    for string in word_bank:
        # remember - substring must be a PREFIX of input target string
        # therefore, must check if substring is found at index 0 of target string
        with contextlib.suppress(ValueError):
            # this context manager prevents a ValueError from being thrown if the substring does not exist in the target string

            # if substring is a prefix of target string
            if target.index(string) == 0:
                # remove the prefix and KEEP GOING!
                new_string = target[len(string) :]
                count += count_construct(
                    target=new_string,
                    word_bank=word_bank,
                    substring_cache=substring_cache,
                )

    # cache count result for speed boost
    substring_cache[target] = count
    return count


if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(
        count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    )
    print(count_construct(("e" * 40) + "f", ["e" * i for i in range(1, 6)]))
