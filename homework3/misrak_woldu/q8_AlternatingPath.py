from collections import deque

# Data Structure: Graph (Adjacency List)
# Algorithm: BFS with state tracking
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)


def shortest_alternating_path(
    edges: list[tuple[str, str, str]],
    origin: str,
    destination: str,
) -> int:
    if origin == destination:
        return 0

    graph = {}

    for start_node, end_node, edge_color in edges:
        if start_node not in graph:
            graph[start_node] = []

        if end_node not in graph:
            graph[end_node] = []

        graph[start_node].append((end_node, edge_color))

    if origin not in graph or destination not in graph:
        return -1

    node_queue = deque()

    # We start with no previous color so either red or blue can be used first
    node_queue.append((origin, None, 0))

    visited_states = set()
    visited_states.add((origin, None))

    while node_queue:
        current_node, previous_color, current_distance = node_queue.popleft()

        for neighbor_node, next_color in graph[current_node]:
            if next_color == previous_color:
                continue

            if (neighbor_node, next_color) in visited_states:
                continue

            if neighbor_node == destination:
                return current_distance + 1

            visited_states.add((neighbor_node, next_color))
            node_queue.append((neighbor_node, next_color, current_distance + 1))

    return -1


def run_tests() -> None:
    edges = [
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

    assert shortest_alternating_path(edges, "A", "E") == 4
    assert shortest_alternating_path(edges, "E", "D") == -1

    # origin equals destination
    assert shortest_alternating_path(edges, "A", "A") == 0

    # direct valid edge
    assert shortest_alternating_path(edges, "A", "B") == 1

    # no origin or destination
    assert shortest_alternating_path(edges, "X", "E") == -1
    assert shortest_alternating_path(edges, "A", "X") == -1

    # simple alternating path
    simple_edges = [
        ("A", "B", "red"),
        ("B", "C", "blue"),
        ("C", "D", "red"),
    ]
    assert shortest_alternating_path(simple_edges, "A", "D") == 3

    # path exists but not alternating
    non_alternating_edges = [
        ("A", "B", "red"),
        ("B", "C", "red"),
    ]
    assert shortest_alternating_path(non_alternating_edges, "A", "C") == -1

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
