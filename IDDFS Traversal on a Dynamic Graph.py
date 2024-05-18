from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def dls(graph, node, target, depth, visited):
    if node == target:
        return True
    if depth <= 0:
        return False
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, target, depth - 1, visited):
                return True
    visited.remove(node)
    return False

def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth):
        visited = set()
        if dls(graph, start, target, depth, visited):
            return True
    return False

graph = defaultdict(list)
edges = int(input("Enter number of edges: "))
for _ in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    add_edge(graph, u, v)

start = int(input("Enter start node: "))
target = int(input("Enter target node: "))
max_depth = int(input("Enter max depth: "))

if iddfs(graph, start, target, max_depth):
    print(f"Path exists from {start} to {target} within depth {max_depth}")
else:
    print(f"No path exists from {start} to {target} within depth {max_depth}")
