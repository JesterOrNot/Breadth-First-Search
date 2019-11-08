from collections import deque

maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width)
             for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append((" S ", (row + 1, col)))
            graph[(row + 1, col)].append((" N ", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append((" E ", (row, col + 1)))
            graph[(row, col + 1)].append((" W ", (row, col)))
    return graph


def find_path_bfs(maze, start: tuple = (2, 1), goal: tuple = (len(maze) - 2, len(maze[0]) - 2)):
    queue = deque([("", start)])  # Path, start node
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"


def debugPath(maze, start: tuple = (2, 1), goal: tuple = (len(maze) - 2, len(maze[0]) - 2)):
    queue = deque([("", start)])  # Path, start node
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            print(current)
            return path
        if current in visited:
            continue
        visited.add(current)
        print(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"


def prettyPrint(maze):
    print("______________________________________")
    for row in range(len(maze)):
        print("|", end="")
        for col in range(len(maze[0])):
            if maze[row][col] == 0:
                print("   ", end="")
            else:
                print("###", end="")
        print("|", end="")
        print()
    print("--------------------------------------")


def debug(maze):
    print("     0  1  2  3  4  5  6  7  8  9 10  11")
    print("   ______________________________________")
    count = 0
    for row in range(len(maze)):
        if count > 9:
            print(count, "|", end="")
        else:
            print(count, " |", end="")
        count += 1
        for col in range(len(maze[0])):
            print("", maze[row][col], "", end="")
        print("|", end="")
        print()
    print("   --------------------------------------")


# prettyPrint(maze)
debug(maze)
print("Start at 10 by 2")
# print(debugPath(maze, (10, 2), (6, 1)))
# print(maze[10][2], maze[2][10])
# print(maze[11])
print(find_path_bfs(maze, (10, 2), (6, 1)))
# print(find_path_bfs(maze, (1, 1)))
