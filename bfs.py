from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            return parent

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]
            new_pos = (new_row, new_col)

            if (0 <= new_row < rows and 0 <= new_col < cols and
                    grid[new_row][new_col] == 0 and new_pos not in visited):
                queue.append(new_pos)
                visited.add(new_pos)
                parent[new_pos] = current

    return None


def construct_path(parent, start, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path



grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

parent = bfs(grid, start, end)

if parent:
    path = construct_path(parent, start, end)
    print("Path from start to destination:", path)
else:
    print("No path found from start to destination.")
