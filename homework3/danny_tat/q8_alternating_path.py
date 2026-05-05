from collections import deque

# Data Structure: Graph, Hashmap, Hashset, Queue
# Algorithm: Breadth-First Search
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Given an origin and destination in a directed graph where edges are blue or red, find the
# length of the shortest alternating-color path, or -1.


def alternatingPath(edges, origin, destination):
    graph = {}
    for u, v, color in edges:
        graph.setdefault(u, []).append((v, color))

    queue = deque([(origin, None, 0)])
    visited = {(origin, None)}

    while queue:
        node, last_color, steps = queue.popleft()
        if node == destination:
            return steps
        for neighbor, color in graph.get(node, []):
            if color != last_color and (neighbor, color) not in visited:
                visited.add((neighbor, color))
                queue.append((neighbor, color, steps + 1))

    return -1


# Testing:
edges = [
    ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"),
    ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"),
    ("E", "C", "red")
]
print(alternatingPath(edges, "A", "E"))  # 4
print(alternatingPath(edges, "E", "D"))  # -1
