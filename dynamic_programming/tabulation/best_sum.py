import contextlib
import copy


def best_sum(change: int, coins: list[int]) -> list[int]:
    """
    best_sum

    Args:
        target (int): _description_
        numbers (list[int]): _description_

    Returns:
        list[int]: _description_
    """

    sums: list[list[int]] = [None] * (change + 1)
    sums[0] = []

    for i in range(len(sums)):
        if sums[i] is None:
            continue
        for coin in coins:
            with contextlib.suppress(IndexError):
                next_num = i + coin
                if sums[next_num] is None:
                    new = copy.copy(sums[i])
                    new.append(coin)
                    sums[next_num] = new
                else:
                    option = copy.copy(sums[i])
                    option.append(coin)
                    sums[next_num] = (
                        option if len(option) < len(sums[next_num]) else sums[next_num]
                    )

    return sums


if __name__ == "__main__":
    print(best_sum(25, [10, 7, 2]))
