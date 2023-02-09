from collections import deque


def breadth_first_traversal(graph: dict, source: str) -> None:
    # breadth first is implemented using a queue, therefore it can only be implemented iteratively
    # this is because recursive calls create an implicit stack data structure that would counteract the queue
    queue = deque()
    queue.append(source)

    while queue:
        current = queue.popleft()
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)


if __name__ == "__main__":
    graph = {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    breadth_first_traversal(graph, "a")
