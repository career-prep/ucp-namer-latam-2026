# Data Structure: Graph
# Algorithm: BFS
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import defaultdict, deque

def alternatingPath(edges, origin, destination):
    graph = defaultdict(list)
    for u, v, color in edges:
        graph[u].append((v, color))
    visited = set()
    queue = deque([(origin, None, 0)])
    visited.add((origin, None))
    while queue:
        node, last_color, dist = queue.popleft()
        if node == destination:
            return dist
        for neighbor, edge_color in graph[node]:
            if edge_color == last_color:
                continue
            state = (neighbor, edge_color)
            if state not in visited:
                visited.add(state)
                queue.append((neighbor, edge_color, dist + 1))

    return -1

edges1 = [
    ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
    ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
    ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")
]
print(alternatingPath(edges1, "A", "E")) 
print(alternatingPath(edges1, "E", "D"))
print(alternatingPath(edges1, "A", "A"))

# Time spent: ~40 minutes
