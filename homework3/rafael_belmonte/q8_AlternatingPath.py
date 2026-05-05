# Data Structure: Graph (directed, edge-colored)
# Algorithm: BFS over an augmented state space (node, last_edge_color)
#
# Standard shortest-path-on-unweighted-graph problem with an extra constraint:
# consecutive edges must alternate in color. We expand each node into two
# states (node, "blue_last") and (node, "red_last"), plus an initial state
# (origin, None) that may step over either color first. BFS guarantees the
# first time we reach the destination is via a shortest path.
#
# Time complexity:  O((V + E) * 2) = O(V + E)
# Space complexity: O(V * 2)

from collections import defaultdict, deque


def alternating_path(edges, origin, destination):
    graph = defaultdict(list)
    for u, v, color in edges:
        graph[u].append((v, color))

    if origin == destination:
        return 0

    visited = set()
    visited.add((origin, None))
    queue = deque([(origin, None, 0)])

    while queue:
        node, last_color, dist = queue.popleft()
        for nbr, color in graph[node]:
            if color == last_color:
                continue  # must alternate
            if nbr == destination:
                return dist + 1
            state = (nbr, color)
            if state not in visited:
                visited.add(state)
                queue.append((nbr, color, dist + 1))
    return -1


# test cases
if __name__ == "__main__":
    edges = [
        ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
        ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
        ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red"),
    ]
    assert alternating_path(edges, "A", "E") == 4
    assert alternating_path(edges, "E", "D") == -1
    assert alternating_path(edges, "A", "A") == 0
    # direct neighbor (single edge counts as alternating)
    assert alternating_path(edges, "A", "B") == 1

    print("yay!!")

# Time spent: ~25 minutes
