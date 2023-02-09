def build_graph(edges: list[list[str]]) -> dict:
    """
    build_graph builds an adjacency list for an undirected graph as a dictionary

    Args:
        edges (list[list[str]]): the edges i.e. list of the graph's edge-connected node-pairs

    Returns:
        dict: the graph's adjacency list
    """

    graph: dict[str, list] = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


def has_path(graph: dict, source: str, dest: str, visited: set = None) -> bool:
    """
    has_path checks if the source -> dest path exists in the input graph

    Args:
        graph (dict): input graph (adjacency list)
        source (str): source node; traversal starting point
        dest (str): dest node; traversal end point

    Returns:
        bool: if the path exists or not
    """

    if visited is None:
        # set is used because it has O(1) insert and lookup time
        visited = set()

    # depth first search iterative - STACK (explicit: list)

    # stack = [source]

    # while stack:
    #     current = stack.pop()
    #     if current in visited:
    #         continue
    #     if current == dest:
    #         return True
    #     visited.add(current)
    #     stack.extend(graph[current])

    # depth first search recursive - STACK (implicit: call stack)

    if source == dest:
        return True

    visited.add(source)

    for neighbour in graph[source]:
        if neighbour in visited:
            continue
        if has_path(graph, neighbour, dest, visited):
            return True

    # breadth first search iterative - QUEUE

    # from collections import deque

    # queue = deque()
    # queue.append(source)

    # while queue:
    #     current = queue.popleft()
    #     if current in visited:
    #         continue
    #     if current == dest:
    #         return True
    #     visited.add(current)
    #     for node in graph[current]:
    #         queue.append(node)

    return False


def undirected_path(edges: list[list[str]], node_a: str, node_b: str) -> bool:
    graph: dict = build_graph(edges)
    return has_path(graph=graph, source=node_a, dest=node_b)


if __name__ == "__main__":
    edges: list[list[int]] = [
        ["i", "j"],
        ["k", "i"],
        ["m", "k"],
        ["k", "l"],
        ["k", "j"],
        ["o", "n"],
    ]
    print(undirected_path(edges=edges, node_a="i", node_b="o"))
