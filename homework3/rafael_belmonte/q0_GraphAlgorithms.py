# Data Structure: Graph (adjacency list/set representation)
# Algorithms: BFS, DFS, Topological Sort (Kahn's), Topological Sort (DFS)
#
# Time complexity:
#   adjacencySet: O(E)
#   bfs / dfs:    O(V + E)
#   topologicalSort (Kahn's): O(V + E)
#   topologicalSortDfs:       O(V + E)
# Space complexity: O(V + E) for the graph; O(V) auxiliary for traversals.

from collections import defaultdict, deque


def adjacencySet(edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        # ensure both endpoints appear as keys (so isolated targets get an empty set)
        if v not in graph:
            graph[v] = set()
    return dict(graph)


def bfs(target, graph):
    if not graph:
        return False
    start = next(iter(graph))
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nbr in graph.get(node, ()):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return False


def dfs(target, graph):
    if not graph:
        return False
    start = next(iter(graph))
    visited = set()

    def visit(node):
        if node in visited:
            return False
        visited.add(node)
        if node == target:
            return True
        for nbr in graph.get(node, ()):
            if visit(nbr):
                return True
        return False

    return visit(start)


def topologicalSort(graph):
    # Kahn's algorithm
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for nbr in graph[node]:
            in_degree[nbr] = in_degree.get(nbr, 0) + 1
            if nbr not in graph:
                # treat dangling target as a node with no outgoing edges
                pass
    # any node referenced as a neighbor but not a key gets in_degree counted above;
    # also make sure they exist in the iteration set
    all_nodes = set(graph.keys()) | set(in_degree.keys())
    queue = deque([n for n in all_nodes if in_degree.get(n, 0) == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in graph.get(node, ()):
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)
    if len(order) != len(all_nodes):
        raise ValueError("Graph contains a cycle; topological sort impossible.")
    return order


def topologicalSortDfs(graph):
    all_nodes = set(graph.keys())
    for node in graph:
        for nbr in graph[node]:
            all_nodes.add(nbr)

    visited = set()      # fully processed
    on_stack = set()     # currently in DFS path (cycle detection)
    order = []           # post-order

    def visit(node):
        if node in on_stack:
            raise ValueError("Graph contains a cycle; topological sort impossible.")
        if node in visited:
            return
        on_stack.add(node)
        for nbr in graph.get(node, ()):
            visit(nbr)
        on_stack.remove(node)
        visited.add(node)
        order.append(node)

    for node in all_nodes:
        if node not in visited:
            visit(node)
    return list(reversed(order))


# test cases
if __name__ == "__main__":
    edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    g = adjacencySet(edges)
    # normalize for printing
    print("adjacencySet:", {k: sorted(v) for k, v in sorted(g.items())})

    # BFS / DFS search (example graph has cycles, so topo on it would fail)
    assert bfs(0, g) is True
    assert dfs(3, g) is True
    assert bfs(99, g) is False
    assert dfs(99, g) is False

    # topo sort needs a DAG
    dag_edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    dag = adjacencySet(dag_edges)

    order_kahn = topologicalSort(dag)
    order_dfs = topologicalSortDfs(dag)

    def is_valid_topo(order, edges):
        pos = {node: i for i, node in enumerate(order)}
        return all(pos[u] < pos[v] for u, v in edges)

    assert is_valid_topo(order_kahn, dag_edges), order_kahn
    assert is_valid_topo(order_dfs, dag_edges), order_dfs
    print("Kahn topo:", order_kahn)
    print("DFS  topo:", order_dfs)

    # cycle detection
    cyclic = adjacencySet([(1, 2), (2, 3), (3, 1)])
    try:
        topologicalSort(cyclic)
        assert False, "expected cycle error"
    except ValueError:
        pass
    try:
        topologicalSortDfs(cyclic)
        assert False, "expected cycle error"
    except ValueError:
        pass

    print("yay!!")

# Time spent: ~50 minutes
