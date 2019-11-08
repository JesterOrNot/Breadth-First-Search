graph2 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

graph = { "A": set(["B", "C", "E", "F"]),
          "B": set(["A", "C", "D"]),
          "C": set(["A", "B"]),
          "D": set(["B"]),
          "E": set(["B", "A"]),
          "F": set(["A"])}
def bfs(graph, start):
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
    queue = [(start,[start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
def bfs_shortest_path(graph, start, end):
    try:
        return next(bfs_path(graph,start,end))
    except StopIteration:
        return None
print(bfs(graph, "A"))
print(list(bfs_path(graph, "F", "D")))
print(bfs_shortest_path(graph, "F", "D"))