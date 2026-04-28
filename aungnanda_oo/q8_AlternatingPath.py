# Question 8: AlternatingPath

# Data Structure: Graph (directed, edge-colored)
# Algorithm: BFS with state = (node, last_color)
#   — guarantees shortest path since BFS explores level by level
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import deque


def alternatingPath(edges, origin, destination):
    blue = {}
    red = {}
    for a, b, color in edges:
        if color == "blue":
            blue.setdefault(a, []).append(b)
        else:
            red.setdefault(a, []).append(b)

    # State: (node, last_color); None means no previous edge (start)
    queue = deque([(origin, None, 0)])
    visited = {(origin, None)}

    while queue:
        node, last_color, dist = queue.popleft()

        if node == destination:
            return dist

        if last_color != "blue":
            for neighbor in blue.get(node, []):
                if (neighbor, "blue") not in visited:
                    visited.add((neighbor, "blue"))
                    queue.append((neighbor, "blue", dist + 1))

        if last_color != "red":
            for neighbor in red.get(node, []):
                if (neighbor, "red") not in visited:
                    visited.add((neighbor, "red"))
                    queue.append((neighbor, "red", dist + 1))

    return -1


# --- Tests ---

edges = [
    ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
    ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
    ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red"),
]

print("A→E:", alternatingPath(edges, "A", "E"))  # 4
print("E→D:", alternatingPath(edges, "E", "D"))  # -1
print("A→A:", alternatingPath(edges, "A", "A"))  # 0

# Simple linear alternating path: A-blue->B-red->C
edges2 = [("A", "B", "blue"), ("B", "C", "red")]
print("A→C (2-hop):", alternatingPath(edges2, "A", "C"))   # 2
print("A→B (1-hop):", alternatingPath(edges2, "A", "B"))   # 1

# No path
edges3 = [("A", "B", "blue"), ("B", "C", "blue")]
print("no alternating path:", alternatingPath(edges3, "A", "C"))  # -1

# Spent a total of 35 mins on this question
