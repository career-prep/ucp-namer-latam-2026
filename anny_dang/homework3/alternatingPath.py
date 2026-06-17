from collections import defaultdict, deque


def alternatingPath(arr, origin, destination):
    """
    Idea:
    Build a directed graph where each edge stores its destination and color.
    Use BFS to find the shortest path, while keeping track of both the current
    node and the color of the last edge used to reach it.
    From each state, only visit outgoing edges whose color is different from
    the previous edge color. If the destination is reached, return the path
    length. If BFS finishes without reaching it, return -1.

    Time complexity: O(V + E)
    Space complexity: O(V + E)
    """
    if origin == destination:
        return 0
    graph = defaultdict(list)
    for u, v, color in arr:
        graph[u].append((v, color))
    
    visited = set()
    queue = deque([("no", origin, 0)])
    while queue:
        color, cur, path = queue.popleft()
        if (cur, color) in visited:
            continue
        if cur == destination:
            return path
        visited.add((cur, color))
        for nei in graph[cur]:
            if (nei[0], nei[1]) not in visited and nei[1] != color:
                queue.append((nei[1], nei[0], path + 1))
    return -1


if __name__ == "__main__":
    example_edges = [
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

    print(alternatingPath(example_edges, "A", "E"))  # Expected: 4
    print(alternatingPath(example_edges, "E", "D"))  # Expected: -1
