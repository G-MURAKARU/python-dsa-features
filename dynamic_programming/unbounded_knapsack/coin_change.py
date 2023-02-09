def coin_change(change: int, coins: list[int]) -> int:
    """
    coin_change returns the number of ways that change can be generated from the coins given

    Args:
        change (int): target change (number)
        coins (list[int]): list of available denominations

    Returns:
        int: number of ways to generate change from coins
    """
    num_coins: int = len(coins)
    change_cache: dict = {}

    def helper_func(current_change: int, index: int, change_cache: dict) -> int:
        """
        helper_func is a recursive helper function

        Args:
            new_change (int): new target change
            index (int): represents a coin denomination from the list of coins
            change_cache (dict): memoisation

        Returns:
            int: number of ways to generate change
        """

        if index == num_coins:
            return 0

        new_change = change - current_change

        if new_change == 0:
            return 1
        if new_change < 0:
            return 0

        if (
            current_change,
            index,
        ) in change_cache:  # index translates to a certain coin denomination
            return change_cache.get((current_change, index))

        result = helper_func(
            current_change + coins[index], index, change_cache
        ) + helper_func(current_change, index + 1, change_cache)
        change_cache[(current_change, index)] = result
        return result

    return helper_func(0, 0, change_cache)


print(coin_change(4, [8, 1, 2, 3]))
