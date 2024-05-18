import random

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_grid(n, obstacle_probability=0.3):
    grid = []
    for _ in range(n):
        row = [0 if random.random() > obstacle_probability else 1 for _ in range(n)]
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))

def is_valid_move(grid, position, visited):
    rows, cols = len(grid), len(grid[0])
    row, col = position
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0 and position not in visited

def dfs(grid, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        current = stack.pop()
        if current == goal:
            return parent

        visited.add(current)

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]
            new_pos = (new_row, new_col)

            if is_valid_move(grid, new_pos, visited):
                stack.append(new_pos)
                parent[new_pos] = current

    return None

def construct_path(parent, start, goal):
    path = []
    current = goal
    while current:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


n = int(input("Enter the grid size (N): "))


grid = generate_grid(n)


print("Generated Grid:")
print_grid(grid)

start = tuple(map(int, input("Enter the start position (row, col): ").split(',')))
goal = tuple(map(int, input("Enter the goal position (row, col): ").split(',')))

if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
    print("Start or goal position is an obstacle.")
else:
    parent = dfs(grid, start, goal)

    if parent:
        path = construct_path(parent, start, goal)
        print("Path from start to goal:", path)
    else:
        print("No path found from start to goal.")
