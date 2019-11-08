"""BFS in Python."""
GRAPH_2 = {'A': set(['B', 'C']),
           'B': set(['A', 'D', 'E']),
           'C': set(['A', 'F']),
           'D': set(['B']),
           'E': set(['B', 'F']),
           'F': set(['C', 'E'])}

GRAPH = {"A": set(["B", "C", "E", "F"]),
         "B": set(["A", "C", "D"]),
         "C": set(["A", "B"]),
         "D": set(["B"]),
         "E": set(["B", "A"]),
         "F": set(["A"])}


def bfs(graph, start):
    """Return visited nodes."""
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex]-visited)
    return visited


def bfs_path(graph, start, end):
    """Return all paths."""
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for i in graph[vertex] - set(path):
            if i == end:
                yield path + [i]
            else:
                queue.append((i, path + [i]))


def bfs_shortest_path(graph, start, end):
    """Find the shortest path with BFS."""
    try:
        return next(bfs_path(graph, start, end))
    except StopIteration:
        return None


print(bfs(GRAPH, "A"))
print(list(bfs_path(GRAPH, "F", "D")))
print(bfs_shortest_path(GRAPH, "F", "D"))
