# def depth_first_traversal(graph: dict, source: str) -> None:
#     # depth first search uses a STACK (see freeCodeCamp video)
#     stack: list[str] = [source]

#     while stack:
#         current = stack.pop()
#         print(current)
#         stack.extend(graph[current])
# print(stack)


def depth_first_traversal(graph: dict, source: str) -> None:
    print(source)

    for neighbour in graph[source]:
        depth_first_traversal(graph=graph, source=neighbour)


if __name__ == "__main__":
    graph = {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    depth_first_traversal(graph, "a")
