# not sure if dijkstra's or nah...


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


def shortest_path(graph: dict, source: str, dest: str) -> int:
    """
    shortest_path finds the length of the shortest path between nodes in a graph

    Args:
        graph (dict): input graph as an adjacency list
        source (str): traversal starting point
        dest (str): traversal end point

    Returns:
        int: length of the shortest path
    """

    # iterative BFS - QUEUE
    from collections import deque

    queue = deque()
    visited = set()

    length = 0
    queue.append((source, length))

    while queue:
        # print(queue)
        current = queue.popleft()
        node, edge = current
        if node in visited:
            continue
        if node == dest:
            return edge
        visited.add(current)
        for neighbour in graph[node]:
            queue.append((neighbour, edge + 1))

    return -1


if __name__ == "__main__":
    edges: list[list[str]] = [
        ["w", "x"],
        ["x", "y"],
        ["z", "y"],
        ["z", "v"],
        ["w", "v"],
        ["v", "u"],
        ["u", "t"],
    ]
    graph = build_graph(edges)
    print(shortest_path(graph=graph, source="w", dest="z"))
