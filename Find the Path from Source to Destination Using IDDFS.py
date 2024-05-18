from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def dls_path(graph, node, target, depth, path, visited):
    path.append(node)
    if node == target:
        return True
    if depth <= 0:
        path.pop()
        return False
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls_path(graph, neighbor, target, depth - 1, path, visited):
                return True
    visited.remove(node)
    path.pop()
    return False

def iddfs_path(graph, start, target, max_depth):
    for depth in range(max_depth):
        visited = set()
        path = []
        if dls_path(graph, start, target, depth, path, visited):
            return path
    return None

graph = defaultdict(list)
edges = int(input("Enter number of edges: "))
for _ in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    add_edge(graph, u, v)

start = int(input("Enter start node: "))
target = int(input("Enter target node: "))
max_depth = int(input("Enter max depth: "))

path = iddfs_path(graph, start, target, max_depth)
if path:
    print(f"Path from {start} to {target} within depth {max_depth}: {path}")
else:
    print(f"No path found from {start} to {target} within depth {max_depth}")
