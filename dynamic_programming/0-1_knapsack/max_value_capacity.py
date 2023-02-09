def max_value_capacity(capacity: int, weights: list[list[int]]) -> int:
    """
    max_value_capacity _summary_

    Args:
        capacity (int): _description_
        weights (list[list[int]]): _description_

    Returns:
        int: _description_
    """

    num_weights: int = len(weights)

    def helper_func(
        target: int, weights: list[list[str]], index: int, current_value: int
    ) -> int:
        """
        helper_func _summary_

        Args:
            target (int): _description_
            weights (list[list[str]]): _description_
            index (int): _description_
            current_value (int): _description_

        Returns:
            int: _description_
        """

        if index >= num_weights:
            return current_value

        new_target = target - weights[index][0]
        if new_target < 0:
            return current_value

        if new_target == 0:
            current_value += weights[index][1]
            return current_value

        return max(
            helper_func(
                new_target, weights, index + 1, current_value + weights[index][1]
            ),
            helper_func(target, weights, index + 1, current_value),
        )

    return helper_func(capacity, weights, 0, 0)


print(max_value_capacity(7, [[1, 2], [2, 3], [3, 2], [3, 4], [4, 5]]))
