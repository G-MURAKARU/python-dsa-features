import itertools


def build_graph_from_grid(grid: list[int]) -> dict:
    """
    build_graph_from_grid builds an adjacency list for all cells in an n x m grid

    Args:
        grid (list[int]): the dimensions of the grid

    Returns:
        dict: an adjacency list of all cells and their neighbouring cells
    """

    rows, cols = grid

    graph = {}

    for row, col in itertools.product(range(rows), range(cols)):
        graph[(row, col)] = []
        if row > 0:
            graph[(row, col)].append((row - 1, col))
        if row < rows - 1:
            graph[(row, col)].append((row + 1, col))
        if col > 0:
            graph[(row, col)].append((row, col - 1))
        if col < cols - 1:
            graph[(row, col)].append((row, col + 1))

    return graph
    # for row in range(rows):
    #     for col in range(cols):
    #         graph[(row, col)] = []
    #         if row > 0:
    #             graph[(row, col)].append((row - 1, col))
    #         if row < rows - 1:
    #             graph[(row, col)].append((row + 1, col))
    #         if col > 0:
    #             graph[(row, col)].append((row, col - 1))
    #         if col < cols - 1:
    #             graph[(row, col)].append((row, col + 1))


def count_islands(grid: list[list[str]], graph: dict) -> int:
    # good thing is accessing an element at a particular index in a list is O(1)

    visited = set()

    island_count = 0

    # iterative depth-first traversal with stack

    for cell in graph:
        add = False
        if cell in visited:
            continue
        # the stack is initialised at the beginning of graph traversal i.e. when an uncharted cell is discovered
        stack: list[tuple] = [cell]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            row, col = current
            if grid[row][col] == "L":
                # this boolean flag ensures that island_count below is incremented only when an uncharted cell is land
                # without it, island_count would increment with every discovered uncharted cell
                # it is put outside the 'while stack' loop to prevent it incrementing every time a land cell is found
                # (multiple land cells could belong to the same island)
                add = True
                stack.extend(graph[current])

        island_count += 1 if add else 0

    return island_count


if __name__ == "__main__":
    grid = [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ]

    grid = [
        ["L", "W", "W", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["W", "L", "W", "L", "W"],
        ["W", "W", "W", "W", "W"],
        ["W", "W", "L", "L", "L"],
    ]

    grid = [
        ["L", "L", "L"],
        ["L", "L", "L"],
        ["L", "L", "L"],
    ]

    grid = [
        ["W", "W"],
        ["W", "W"],
        ["W", "W"],
    ]

    grid_dimensions = [len(grid), len(grid[0])]
    graph = build_graph_from_grid(grid_dimensions)
    islands = count_islands(grid, graph)
    print(islands)
