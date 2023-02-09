def build_graph(related: list[str]) -> dict:
    """
    build_graph builds a graph's adjacency list (dict) from an input list of binary strings
    Args:
        related (list[str]): input list of strings depicting edge-connected nodes

    Returns:
        dict: graph's adjacency list
    """

    return {
        index: [i for i in range(len(person)) if (i != index and person[i] == "1")]
        for index, person in enumerate(related)
    }


def connected_groups(relationships: dict) -> int:
    """
    connected_groups returns the number of connections (direct or transitive relationships) present among a group of people

    Args:
        relationships (dict): adjacency list depicting direct relationships between people

    Returns:
        int: number of connections
    """

    # this is a count-connected-components problem with an undirected graph

    # to keep track of the person whose relationships we have already explored
    visited = set()

    # using an iterative, stack-based DFS
    stack: list = []

    # keeping track of number of connections
    connections = 0

    # DEPTH FIRST SEARCH
    for person in relationships:
        if person in visited:
            continue
        stack.append(person)
        while stack:
            current: int = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            stack.extend(relationships[current])
        connections += 1

    return connections


if __name__ == "__main__":
    related: list[str] = ["1100", "1110", "0110", "0001"]
    related: list[str] = ["10000", "01000", "00100", "00010", "00001"]
    related: list[str] = ["110", "110", "001"]
    relationships: dict = build_graph(related)
    groups: int = connected_groups(relationships)
    print(groups)
