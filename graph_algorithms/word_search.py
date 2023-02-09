import itertools


def word_search(grid: list[list[str]], word: str) -> bool:
    """
    word_search

    Args:
        grid (list[list[str]]): _description_

    Returns:
        bool: _description_
    """

    visited = set()

    word_length = len(word)

    def explore_grid(cell: tuple[int], index: int) -> bool:
        """
        explore_grid _summary_

        Args:
            cell (tuple[int]): _description_

        Returns:
            bool: _description_
        """

        if index == word_length:
            return True

        if cell in visited:
            visited.clear()
            return False

        # unpack input coordinate to row index and col index
        row, col = cell

        # guard for out-of-bounds coordinates first, prevent IndexError (can use try-except too but overkill)
        row_out_of_bounds = row < 0 or row >= len(grid)
        col_out_of_bounds = col < 0 or col >= len(grid[0])

        if row_out_of_bounds or col_out_of_bounds:
            visited.clear()
            return False

        if grid[row][col] != word[index]:
            visited.clear()
            return False

        visited.add(cell)

        return any(
            [
                explore_grid((row - 1, col), index + 1),
                explore_grid((row + 1, col), index + 1),
                explore_grid((row, col - 1), index + 1),
                explore_grid((row, col + 1), index + 1),
            ]
        )

    for cell in itertools.product(range(len(grid)), range(len(grid[0]))):
        if explore_grid(cell, index=0):
            return True

    return False


grid: list[list[str]] = [
    ["a", "b", "c", "e"],
    ["s", "f", "c", "s"],
    ["a", "d", "e", "e"],
]
print(word_search(grid, "abfsad"))
