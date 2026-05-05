from collections import deque

# Data Structure: Graph (Adjacency Set)
# Algorithms:
# - BFS (Breadth-First Search)
# - DFS (Depth-First Search)
# - Topological Sort (Kahn’s Algorithm - BFS)
# - Topological Sort (DFS + cycle detection)

# Time Complexity:
# - Building graph: O(E)
# - BFS: O(V + E)
# - DFS: O(V + E)
# - Topological Sort: O(V + E)

# Space Complexity:
# - Graph storage: O(V + E)
# - BFS queue / DFS recursion: O(V)

def adjacency_set(edges: list[tuple[int, int]]) -> dict[int, set[int]]:
    graph = {}

    for start_node, end_node in edges:
        if start_node not in graph:
            graph[start_node] = set()

        if end_node not in graph:
            graph[end_node] = set()

        graph[start_node].add(end_node)

    return graph


def bfs(target: int, graph: dict[int, set[int]]) -> bool:
    if not graph:
        return False

    visited_nodes = set()

    for start_node in graph:
        if start_node in visited_nodes:
            continue

        node_queue = deque([start_node])
        visited_nodes.add(start_node)

        while node_queue:
            current_node = node_queue.popleft()

            if current_node == target:
                return True

            for neighbor_node in graph[current_node]:
                if neighbor_node not in visited_nodes:
                    visited_nodes.add(neighbor_node)
                    node_queue.append(neighbor_node)

    return False


def dfs(target: int, graph: dict[int, set[int]]) -> bool:
    if not graph:
        return False

    visited_nodes = set()

    for start_node in graph:
        if start_node not in visited_nodes:
            if dfs_helper(start_node, target, graph, visited_nodes):
                return True

    return False


def dfs_helper(
    current_node: int,
    target: int,
    graph: dict[int, set[int]],
    visited_nodes: set[int],
) -> bool:
    if current_node == target:
        return True

    visited_nodes.add(current_node)

    for neighbor_node in graph[current_node]:
        if neighbor_node not in visited_nodes:
            if dfs_helper(neighbor_node, target, graph, visited_nodes):
                return True

    return False


def topological_sort_kahn(graph: dict[int, set[int]]) -> list[int]:
    in_degree = {node: 0 for node in graph}

    for start_node in graph:
        for neighbor_node in graph[start_node]:
            in_degree[neighbor_node] += 1

    node_queue = deque()

    for node, degree in in_degree.items():
        if degree == 0:
            node_queue.append(node)

    sorted_order = []

    while node_queue:
        current_node = node_queue.popleft()
        sorted_order.append(current_node)

        for neighbor_node in graph[current_node]:
            in_degree[neighbor_node] -= 1

            if in_degree[neighbor_node] == 0:
                node_queue.append(neighbor_node)

    if len(sorted_order) != len(graph):
        return []

    return sorted_order


def topological_sort_dfs(graph: dict[int, set[int]]) -> list[int]:
    visited_nodes = set()
    visiting_nodes = set()
    sorted_order = []

    for node in graph:
        if node not in visited_nodes:
            if has_cycle_dfs(node, graph, visited_nodes, visiting_nodes, sorted_order):
                return []

    sorted_order.reverse()
    return sorted_order


def has_cycle_dfs(
    current_node: int,
    graph: dict[int, set[int]],
    visited_nodes: set[int],
    visiting_nodes: set[int],
    sorted_order: list[int],
) -> bool:
    if current_node in visiting_nodes:
        return True

    if current_node in visited_nodes:
        return False

    visiting_nodes.add(current_node)

    for neighbor_node in graph[current_node]:
        if has_cycle_dfs(neighbor_node, graph, visited_nodes, visiting_nodes, sorted_order):
            return True

    visiting_nodes.remove(current_node)
    visited_nodes.add(current_node)
    sorted_order.append(current_node)

    return False


def is_valid_topological_order(order: list[int], graph: dict[int, set[int]]) -> bool:
    if len(order) != len(graph):
        return False

    position = {}

    for index, node in enumerate(order):
        position[node] = index

    for start_node in graph:
        for end_node in graph[start_node]:
            if position[start_node] > position[end_node]:
                return False

    return True


def run_tests() -> None:
    edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    graph = adjacency_set(edges)

    assert graph == {
        0: set(),
        1: {2, 3},
        2: {0, 3},
        3: {2},
    }

    assert bfs(3, graph) is True
    assert bfs(99, graph) is False

    assert dfs(0, graph) is True
    assert dfs(99, graph) is False

    dag_edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    dag_graph = adjacency_set(dag_edges)

    kahn_order = topological_sort_kahn(dag_graph)
    dfs_order = topological_sort_dfs(dag_graph)

    assert is_valid_topological_order(kahn_order, dag_graph) is True
    assert is_valid_topological_order(dfs_order, dag_graph) is True

    cycle_edges = [(1, 2), (2, 3), (3, 1)]
    cycle_graph = adjacency_set(cycle_edges)

    assert topological_sort_kahn(cycle_graph) == []
    assert topological_sort_dfs(cycle_graph) == []

    assert adjacency_set([]) == {}

    print("All tests passed")


if __name__ == "__main__":
    run_tests()

