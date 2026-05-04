# Data Structure: Graph + BFS
# Technique: BFS 
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import deque

def alternatingPath(edges, origin, destination):
    # build separate adjacency lists for blue and red edges
    blue = {}
    red  = {}

    for u, v, color in edges:
        if color == "blue":
            if u not in blue:
                blue[u] = []
            blue[u].append(v)
        else:
            if u not in red:
                red[u] = []
            red[u].append(v)

    queue   = deque([(origin, None, 0)])   # (node, last_color, steps)
    visited = set()
    visited.add((origin, None))

    while queue:
        node, lastColor, steps = queue.popleft()

        if node == destination:
            return steps

        # try blue edges if last color wasn't blue
        if lastColor != "blue":
            for neighbor in blue.get(node, []):
                if (neighbor, "blue") not in visited:
                    visited.add((neighbor, "blue"))
                    queue.append((neighbor, "blue", steps + 1))

        # try red edges if last color wasn't red
        if lastColor != "red":
            for neighbor in red.get(node, []):
                if (neighbor, "red") not in visited:
                    visited.add((neighbor, "red"))
                    queue.append((neighbor, "red", steps + 1))

    return -1


edges = [
    ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
    ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
    ("A", "D", "red"),  ("D", "E", "red"), ("E", "C", "red")
]

# Test 1: A -> E, expect 4  (A->D red, D->C blue, C->B red, B->E blue)
print(alternatingPath(edges, "A", "E"))   # 4

# Test 2: E -> D, expect -1  (E->C red, C->B red — not alternating)
print(alternatingPath(edges, "E", "D"))   # -1

# Test 3: same origin and destination -> 0
print(alternatingPath(edges, "A", "A"))   # 0

# Test 4: direct single edge
edges2 = [("X", "Y", "blue")]
print(alternatingPath(edges2, "X", "Y")) # 1

# Test 5: no path at all
edges3 = [("A", "B", "blue"), ("C", "D", "red")]
print(alternatingPath(edges3, "A", "D")) # -1

# Time spent: ~40 minutes