from collections import defaultdict


def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def color_graph(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True


def graph_coloring(graph, states):
    colors = {}
    colored_states = {}
    for state in states:
        colors[state] = None

    for state in states:
        for color in range(len(states)):
            if color_graph(graph, colors, state, color):
                colors[state] = color
                colored_states[state] = color
                break

    return colored_states


adjacency_list = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales'],
    'Tasmania': []
}

states = list(adjacency_list.keys())

graph = defaultdict(list)
for state, neighbors in adjacency_list.items():
    for neighbor in neighbors:
        add_edge(graph, state, neighbor)

colored_states = graph_coloring(graph, states)

print("Colored states:")
for state, color in colored_states.items():
    print(f"{state}: Color {color}")
