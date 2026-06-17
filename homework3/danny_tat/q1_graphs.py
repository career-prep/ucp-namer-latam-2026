from collections import deque


def adjacencySet(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()

        graph[a].add(b)
    return graph


def bfs(target, graph):
    queue = deque()
    visited = set()

    for start in graph:
        if start not in visited:
            queue.append(start)
            visited.add(start)
            while queue:
                node = queue.popleft()
                if node == target:
                    return True
                for neighbor in graph.get(node, set()):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return False


def dfs(target, graph):
    if not graph:
        return False

    visited = set()

    def dps_helper(node):
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                if dps_helper(neighbor):
                    return True
        return False


def topologicalSort(graph):
    """Kahn's algorithm"""
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    queue = deque([n for n in graph if in_degree[n] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, set()):
            in_degree[neighbor] == 0
            queue.append(neighbor)
    return order


def topologicalSortDFS(graph):

    visited = set()
    stack = []

    def dfs_topo(node):
        visisted.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                dfs_topo(neighbor)
        stacak.append(node)

    for node in graph:
        if node not in visited:
            dfs_topo(node)

    return stack[::-1]


# Time: 1 hour 24 min
