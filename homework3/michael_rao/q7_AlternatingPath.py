# Data structure: Graph - BFS
# Time: O(V + E)
# Space: O(V + E)

from collections import deque


def shortest_alternating_path(edges, origin, destination):
    graph = {}
    for u, v, color in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, color))
        if v not in graph:
            graph[v] = []

    q = deque([(origin, None, 0)])  # (node, previous edge color, distance)
    visited = {(origin, None)}

    while q:
        node, prev_color, dist = q.popleft()
        if node == destination:
            return dist
        for nxt, color in graph.get(node, []):
            if prev_color is not None and color == prev_color:
                continue
            state = (nxt, color)
            if state not in visited:
                visited.add(state)
                q.append((nxt, color, dist + 1))
    return -1


edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]
print("Correct:", 4)
print("Output: ", shortest_alternating_path(edges, "A", "E"))
print()

print("Correct:", -1)
print("Output: ", shortest_alternating_path(edges, "E", "D"))
print()

print("Correct:", 0)
print("Output: ", shortest_alternating_path(edges, "A", "A"))
print()

# time taken: 23 min
