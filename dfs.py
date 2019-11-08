"""DFS in python."""

GRAPH = {"A": set(["B", "C", "E", "F"]),
         "B": set(["A", "C", "D"]),
         "C": set(["A", "B"]),
         "D": set(["B"]),
         "E": set(["B", "A"]),
         "F": set(["A"])}


def dfs(graph, start):
    """DFS algorithm."""
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(graph[node] - visited)
    return visited


print(dfs(GRAPH, "A"))
