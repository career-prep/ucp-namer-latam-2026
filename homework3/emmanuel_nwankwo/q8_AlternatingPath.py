# Data Structure: Graph
# Algorithm: Breadth-first search
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import deque

def alternating_path(edges, origin, destination):
    # Build graph
    graph = {}
    for u, v, color in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, color))

    q = deque([(origin, None, 0)])
    visited = set()

    while q:
        node, last_color, dist = q.popleft()

        if node == destination:
            return dist

        if (node, last_color) in visited:
            continue
        visited.add((node, last_color))

        for neighbor, color in graph.get(node, []):
            if color != last_color:
                q.append((neighbor, color, dist + 1))

    return -1


# Time Taken: 14mins 49secs

# Test Cases
edges = [("A","B","blue"),("A","C","red"),("B","D","blue"),("B","E","blue"),
         ("C","B","red"),("D","C","blue"),("A","D","red"),("D","E","red"),("E","C","red")]

print(alternating_path(edges, "A", "E"))
print(alternating_path(edges, "E", "D"))

# Edge Cases
print(alternating_path([], "A", "B"))
print(alternating_path([("A","B","red")], "A", "B"))
print(alternating_path([("A","B","red"),("B","C","red")], "A", "C"))