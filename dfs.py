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
            stack.extend(GRAPH[node] - visited)
    return visited


def dfs_path(graph, start, end):
    """Return all DFS paths."""
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for following in graph[node] - set(path):
            if following == end:
                yield path + [following]
            else:
                stack.append((following, path + [following]))


print(dfs(GRAPH, "A"))
print(list(dfs_path(GRAPH, "F", "D")))
