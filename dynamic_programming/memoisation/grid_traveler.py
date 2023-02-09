from functools import cache


# @cache
def grid_traveler(rows: int, cols: int, grid_cache: dict = None) -> int:
    """
    grid_traveler finds the number of unique paths through an n x m grid

    Args:
        rows (int): number of grid rows
        cols (int): number of grid columns

    Returns:
        int: number of unique paths
    """

    if grid_cache is None:
        grid_cache = {}

    if rows == 0 or cols == 0:
        return 0

    if rows == 1 or cols == 1:
        return 1

    if (rows, cols) in grid_cache:
        return grid_cache.get((rows, cols))

    # found by drawing the function tree structure with left branch going down and right branch going right
    result = grid_traveler((rows - 1), cols, grid_cache) + grid_traveler(
        rows, (cols - 1), grid_cache
    )
    grid_cache[(rows, cols)] = result
    return result


if __name__ == "__main__":
    print(grid_traveler(3, 4))
