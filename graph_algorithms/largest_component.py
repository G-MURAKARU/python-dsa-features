def explore(graph: dict, source: int, visited: set, current_length: int = 0) -> int:
    """
    explore traverses a graph beginning at the [source] node

    Args:
        graph (dict): input graph as an adjacency list
        source (int): traversal start point
        visited (set): set of visited nodes (prevents infinite traversal if cycles present)

    Returns:
        int: length of the path. 0 if charted path
    """

    # * if the node is visited, then the length of the new path == 0 i.e. no new path exists
    if source in visited:
        return 0
    visited.add(source)

    return 1 + sum(
        explore(graph, neighbour, visited, current_length)
        for neighbour in graph[source]
        if neighbour not in visited
    )


def largest_component(graph: dict, visited: set = None) -> int:
    """
    largest_component finds the size of the largest 'sub-graph' in input graph using recursive DFS

    Args:
        graph (dict): input graph as an adjacency list
        visited (set, optional): set of (already-)visited nodes. Defaults to None.

    Returns:
        int: size of largest/longest 'sub-graph'
    """

    max_length = 0

    if visited is None:
        visited = set()

    for node in graph:
        # if node in visited:
        #     continue
        length = explore(graph=graph, source=node, visited=visited)
        max_length = max(length, max_length)

    return max_length


if __name__ == "__main__":
    graph: dict = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }

    graph: dict = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1],
    }

    print(largest_component(graph=graph))
