from collections import deque

# Data Structure: Graph (Adjacency List)
# Algorithm: BFS (Shortest Path)
# Time Complexity: O(cities + roads)
# Space Complexity: O(cities + roads)


def shortest_vacation_path(
    roads: list[tuple[str, str]],
    start: str,
    destination: str,
) -> int:
    if start == destination:
        return 0

    graph = {}

    for city1, city2 in roads:
        if city1 not in graph:
            graph[city1] = []

        if city2 not in graph:
            graph[city2] = []

        graph[city1].append(city2)
        graph[city2].append(city1)

    if start not in graph or destination not in graph:
        return -1

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current_city, distance = queue.popleft()

        if current_city == destination:
            return distance

        for neighbor in graph[current_city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


def run_tests() -> None:
    roads = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("A", "F"),
        ("F", "E"),
    ]

    assert shortest_vacation_path(roads, "A", "E") == 2
    assert shortest_vacation_path(roads, "A", "D") == 3
    assert shortest_vacation_path(roads, "B", "F") == 2

    # same start and destination
    assert shortest_vacation_path(roads, "A", "A") == 0

    # unreachable
    roads2 = [
        ("A", "B"),
        ("C", "D"),
    ]
    assert shortest_vacation_path(roads2, "A", "D") == -1

    # missing nodes
    assert shortest_vacation_path(roads, "X", "E") == -1
    assert shortest_vacation_path(roads, "A", "X") == -1

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
