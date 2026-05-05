# Data Structure: Graph (adjacency list/set)
# Algorithm: BFS, DFS, Topological Sort (Kahn's and DFS)
# Time Complexity: O(V + E) for all traversals
# Space Complexity: O(V + E)

from collections import defaultdict, deque


def adjacencySet(edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        if v not in graph:
            graph[v] = set()
    return graph


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


def topologicalSort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    queue = deque([n for n in in_degree if in_degree[n] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return []
    return result


def topologicalSortDfs(graph):
    visited = set()
    result = []

    def helper(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                helper(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            helper(node)

    result.reverse()
    return result


edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
graph = adjacencySet(edges)
for node in sorted(graph.keys()):
    print(f"{node}: {sorted(graph[node])}")

print(bfs(0, graph))   
print(bfs(99, graph))   
print(dfs(3, graph))    
print(dfs(99, graph))   

dag_edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
dag = adjacencySet(dag_edges)
print(topologicalSort(dag))
print(topologicalSortDfs(dag))

# Time spent: 50 minutes
