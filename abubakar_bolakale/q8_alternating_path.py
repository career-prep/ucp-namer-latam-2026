# Data structure: Graph (adjacency with colored edges)
# Algorithm: Breadth-first search on (node, last color)

from collections import deque, defaultdict


def alternating_path(edges, start, goal):
    g = defaultdict(list)
    for u, v, c in edges:
        g[u].append((v, c))
    dq = deque([(start, 0, None)])
    seen = set()
    while dq:
        u, d, lc = dq.popleft()
        if u == goal:
            return d
        for v, c in g[u]:
            if c != lc and (v, c) not in seen:
                seen.add((v, c))
                dq.append((v, d + 1, c))
    return -1


if __name__ == "__main__":
    e = [
        ("A", "B", "blue"),
        ("A", "C", "red"),
        ("B", "D", "blue"),
        ("B", "E", "blue"),
        ("C", "B", "red"),
        ("D", "C", "blue"),
        ("A", "D", "red"),
        ("D", "E", "red"),
        ("E", "C", "red"),
    ]
    print("=== Spec A -> E (expect 4) ===")
    print(" ", alternating_path(e, "A", "E"))

    print("=== Spec E -> D (expect -1) ===")
    print(" ", alternating_path(e, "E", "D"))

    print("=== Same node ===")
    print(" ", alternating_path(e, "A", "A"))

    print("=== No edges ===")
    print(" ", alternating_path([], "A", "B"))

    print("=== Two nodes alternating colors ===")
    simple = [("X", "Y", 0), ("Y", "Z", 1)]
    print(" ", alternating_path(simple, "X", "Z"))

    print("=== Same color twice in a row (blocked) ===")
    bad = [("X", "Y", 1), ("Y", "Z", 1)]
    print(" ", alternating_path(bad, "X", "Z"))


# Time complexity: O(V + E)
# Space complexity: O(V + E)
# Time spent: 30 minutes
