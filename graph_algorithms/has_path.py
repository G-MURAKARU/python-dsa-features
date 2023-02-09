def has_path(graph: dict, source: str, dest: str) -> bool:
    """
    has_path checks if a path exists between the source node and the destination node

    Args:
        graph (dict): a directed, acyclic graph
        source (str): traversal starting point
        dest (str): supposed traversal end point

    Returns:
        bool: whether the source -> destination path exists
    """

    # using depth first search iteration - stack
    # stack: list[str] = [source]

    # while stack:
    #     current = stack.pop()
    #     if current == dest:
    #         return True
    #     stack.extend(graph[current])

    # using depth first search recursion - stack
    # if source == dest:
    #     return True

    # return any(has_path(graph, element, dest) for element in graph[source])

    # using breadth first search - queue
    from collections import deque

    queue = deque()
    queue.append(source)

    while queue:
        current = queue.popleft()
        if current == dest:
            return True
        # if above is not true, we need to check current's neighbours
        for element in graph[current]:
            queue.append(element)

    return False


if __name__ == "__main__":
    graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}
    print(has_path(graph, "j", "f"))
    print(has_path(graph, "f", "k"))
