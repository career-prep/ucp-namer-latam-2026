from collections import deque

def AlternatingPath(edges, origin, destination):

    graph = {}

    for start, end, color in edges:

        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []

        graph[start].append((end,color))

    queue = deque()
    queue.append((origin, None, 0))

    visited = set()
    visited.add((origin, None))

    while queue:
        node, last_color, distance = queue.popleft()

        if node == destination:
            return distance

        for neighbor, color in graph[node]:
            # First move is always allowed because last_color is None
            # After that, colors must alternate
            if color != last_color:
                state = (neighbor, color)

                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, color, distance + 1))

    return -1

edges = [
    ("A", "B", "blue"),
    ("A", "C", "red"),
    ("B", "D", "blue"),
    ("B", "E", "blue"),
    ("C", "B", "red"),
    ("D", "C", "blue"),
    ("A", "D", "red"),
    ("D", "E", "red"),
    ("E", "C", "red")
]

# origin = "A"
# destination = "E"
# Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))

# origin = "E"
# destination = "D"
# Output: -1 (only path is: E→C (red), C→B (red), B→D (blue))

# print(AlternatingPath(edges, origin, destination))

#  40