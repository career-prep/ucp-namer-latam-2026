from collections import deque


def adjacencySet(edges):  # O(V + E)
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
    return graph


# Algorithm: Breadth-First Search
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def bfs(target, graph):
    visited = set()
    for start in graph:
        if start in visited:
            continue
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return False


# Algorithm: Depth-First Search (recursive)
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def dfs(target, graph):
    visited = set()

    def helper(node):
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if helper(neighbor):
                    return True
        return False

    for start in graph:
        if start not in visited:
            if helper(start):
                return True
    return False


# Algorithm: Kahn's algorithm (BFS-based topological sort using in-degrees)
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def topologicalSort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return []  # cycle detected, no valid topological order
    return result


# Algorithm: DFS-based topological sort (reverse post-order)
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def topologicalSortDfs(graph):
    visited = set()
    on_stack = set()
    result = []
    has_cycle = [False]

    def helper(node):
        if has_cycle[0]:
            return
        visited.add(node)
        on_stack.add(node)
        for neighbor in graph[node]:
            if neighbor in on_stack:
                has_cycle[0] = True
                return
            if neighbor not in visited:
                helper(neighbor)
        on_stack.remove(node)
        result.append(node)

    for node in graph:
        if node not in visited:
            helper(node)

    if has_cycle[0]:
        return []
    return result[::-1]


def printGraph(graph):
    print("{")
    for node in sorted(graph):
        print(f"    {node}: {sorted(graph[node])}")
    print("}")


print("GraphAlgorithms Results:")

edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
g = adjacencySet(edges)
printGraph(g)

print(bfs(0, g))
print(bfs(99, g))
print(dfs(3, g))
print(dfs(99, g))

# DAG used for topological sort tests
dag_edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
dag = adjacencySet(dag_edges)
printGraph(dag)

print(topologicalSort(dag))
print(topologicalSortDfs(dag))

# Graph g contains the cycle 2 -> 3 -> 2, so both should return []
print(topologicalSort(g))
print(topologicalSortDfs(g))
