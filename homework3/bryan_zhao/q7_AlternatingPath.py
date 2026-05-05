# Data Structure: Graph
# Algorithm: BFS
# Time Complexity: O(V + E) since each node is visited at most once
# Space Complexity: O(V + E) to store the graph and seen states

from collections import deque, defaultdict

EDGES = [
    ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), 
    ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), 
    ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")
]

def alternating_path(origin, destination):
    graph = defaultdict(list)
    for u, v, color in EDGES:
        graph[u].append((v, color))

    # Stores (current node, last color, current distance)
    queue = deque([(origin, None, 0)])

    # Stores (node, last color)
    seen = set([origin, None])

    while queue:
        u, last_color, dist = queue.popleft()

        if u == destination:
            return dist
        
        for v, color in graph[u]:
            if color != last_color:
                if (v, color) not in seen:
                    seen.add((v, color))
                    queue.append((v, color, dist + 1))
    
    return -1

print(alternating_path('A', 'E'))
print(alternating_path('E', 'D'))

# Time Spent: 35 min