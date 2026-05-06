# Algorithm: BFS over augmented states (node, last_color used to arrive)
# Each undirected step requires the next edge's color to differ from the previous one.
# Time Complexity: O(V + E)  (each (node, color) state is visited at most once)
# Space Complexity: O(V + E)

from collections import deque


def alternatingPath(edges, origin, destination):
    graph = {}
    for u, v, color in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, color))

    if origin == destination:
        return 0
    if origin not in graph:
        return -1

    queue = deque([(origin, None, 0)])
    visited = {(origin, None)}

    while queue:
        node, last_color, dist = queue.popleft()
        if node not in graph:
            continue
        for neighbor, color in graph[node]:
            if color == last_color:
                continue
            if neighbor == destination:
                return dist + 1
            state = (neighbor, color)
            if state not in visited:
                visited.add(state)
                queue.append((neighbor, color, dist + 1))
    return -1


print("AlternatingPath Results:")

edges = [
    ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
    ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
    ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red"),
]
print(alternatingPath(edges, "A", "E"))
print(alternatingPath(edges, "E", "D"))
print(alternatingPath(edges, "A", "A"))
print(alternatingPath(edges, "A", "Z"))
print(alternatingPath(edges, "A", "C"))
print(alternatingPath(edges, "A", "B"))
