import itertools


def explore_island(grid: list[list[int]], cell: tuple[int], visited: set) -> int:
    """
    explore_island finds the size of an explored island

    Args:
        grid (list[list[int]]): simulation of a body of water
        cell (tuple[int]): grid coordinate
        visited (set): set containing already visited cells

    Returns:
        int: size of the explored island
    """

    # check that input cell is uncharted
    if cell in visited:
        return 0

    visited.add(cell)

    # unpack input coordinate to row index and col index
    row, col = cell

    # guard for out-of-bounds coordinates first, prevent IndexError (can use try-except too but overkill)
    row_out_of_bounds = row < 0 or row >= len(grid)
    col_out_of_bounds = col < 0 or col >= len(grid[0])

    if row_out_of_bounds or col_out_of_bounds:
        return 0

    # begin recursive DFS only for land cells
    if grid[row][col] == "W":
        return 0

    island_size = 1 + explore_island(grid=grid, cell=(row - 1, col), visited=visited)
    island_size += explore_island(grid=grid, cell=(row + 1, col), visited=visited)
    island_size += explore_island(grid=grid, cell=(row, col + 1), visited=visited)
    island_size += explore_island(grid=grid, cell=(row, col - 1), visited=visited)

    return island_size


def find_smallest_island(grid: list[list[int]]) -> int:
    """
    find_smallest_island finds the smallest island in a body of water represented by an n x m grid

    Args:
        grid (list[list[int]]): grid simulating a body of water

    Returns:
        int: size of the smallest island
    """

    # using a recursive depth first search for this one, implicit stack

    # keeping track of already-visited cells
    visited = set()

    # keeping track of island sizes, starting with largest size
    smallest_island_size = float("inf")
    # smallest_island_size = 0

    # need some iterative code to traverse all cells on the grid
    for cell in itertools.product(range(len(grid)), range(len(grid[0]))):
        current_island_size = explore_island(grid, cell, visited)
        if current_island_size > 0:
            smallest_island_size = min(smallest_island_size, current_island_size)

    return smallest_island_size if smallest_island_size != float("inf") else "no island"


if __name__ == "__main__":
    grid = [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ]

    # grid = [
    #     ["L", "W", "W", "L", "W"],
    #     ["L", "W", "W", "L", "L"],
    #     ["W", "L", "W", "L", "W"],
    #     ["W", "W", "W", "W", "W"],
    #     ["W", "W", "L", "L", "L"],
    # ]

    # grid = [
    #     ["L", "L", "L"],
    #     ["L", "L", "L"],
    #     ["L", "L", "L"],
    # ]

    # grid = [
    #     ["W", "W"],
    #     ["W", "W"],
    #     ["W", "W"],
    # ]

    print(find_smallest_island(grid=grid))
