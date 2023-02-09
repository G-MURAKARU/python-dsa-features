def check_anagrams(first_string: str, second_string: str):
    """
    check_anagrams checks if two strings are valid anagrams

    Args:
        first_string (str): first input string
        second_string (str): second input string
    """
    # from collections import Counter
    # if len(first_string) != len(second_string) or len(set(first_string)) != len(
    #     set(second_string)
    # ):
    #     return False

    # first_dict = Counter(first_string)
    # second_dict = Counter(second_string)

    # return first_dict == second_dict

    # * anagrams have the same lexicographically sorted strings
    if len(first_string) != len(second_string):
        return False
    return sorted(first_string) == sorted(second_string)


print(check_anagrams("spandex", "expands"))
print(check_anagrams("salesmen", "nameless"))
