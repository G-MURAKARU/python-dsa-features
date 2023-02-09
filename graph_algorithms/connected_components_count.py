def connected_components_count(graph: dict, visited: set = None) -> int:
    """
    connected_components_count finds the number of 'sub-graphs' in the given graph using iterative DFS

    Args:
        graph (dict): input graph as an adjacency list
        visited (set, optional): set of (already-)visited nodes. Defaults to None.

    Returns:
        int: number of 'sub-graphs
    """
    if visited is None:
        visited = set()

    # nodes = set(graph.keys())
    # * track number of sub-graphs
    count = 0

    # depth first search iterative - STACK
    # while nodes:
    #     removed = nodes.pop()
    # * iterating through all the nodes in the graph
    for node in graph:
        # * if the node was already visited, ignore it
        if node in visited:
            continue
        # stack: list = [removed]
        # * DFS, stack used for traversal
        stack: list = [node]
        # * for as long as the stack is not empty, traversal continues
        # this ensures that all paths emanating from the given node are explored
        while stack:
            # * classic undirected graph iterative DFS
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            # for n in graph[node]:
            # nodes.discard(n)
            stack.extend(graph[node])
        # * since this iteration began with an uncharted node, it translates to having found a new component
        # hence component count is incremented
        count += 1

    return count


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

    # graph: dict = {
    #     3: [],
    #     4: [6],
    #     6: [4, 5, 7, 8],
    #     8: [6],
    #     7: [6],
    #     5: [6],
    #     1: [2],
    #     2: [1],
    # }

    print(connected_components_count(graph=graph))
