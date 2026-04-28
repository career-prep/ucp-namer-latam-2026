# Question 1: Graph Algorithms Using Adjacency List/Set Representation

# Builds adjacency set from edge list, then implements BFS, DFS,
# topological sort via Kahn's algorithm, and topological sort via DFS.

# Time Complexity:
#   adjacencySet: O(E)
#   bfs/dfs: O(V + E)
#   topologicalSort (Kahn's): O(V + E)
#   topologicalSortDfs: O(V + E)
# Space Complexity: O(V + E) for all

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
    visited = set()
    queue = deque()
    for node in graph:
        if node not in visited:
            visited.add(node)
            queue.append(node)
            while queue:
                curr = queue.popleft()
                if curr == target:
                    return True
                for neighbor in graph.get(curr, set()):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    return False
# Time Complexity = O(V + E), Space Complexity = O(V)


def dfs(target, graph):
    visited = set()

    def _dfs(node):
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                if _dfs(neighbor):
                    return True
        return False

    for node in graph:
        if node not in visited:
            if _dfs(node):
                return True
    return False
# Time Complexity = O(V + E), Space Complexity = O(V)


def topologicalSort(graph):
    # Kahn's algorithm (BFS-based)
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, set()):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result
# Time Complexity = O(V + E), Space Complexity = O(V)


def topologicalSortDfs(graph):
    visited = set()
    stack = []

    def _dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                _dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            _dfs(node)
    return stack[::-1]
# Time Complexity = O(V + E), Space Complexity = O(V)


# --- Tests ---

edges1 = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
g1 = adjacencySet(edges1)
print("adjacencySet:", {k: sorted(v) for k, v in sorted(g1.items())})
# Expected: {0: [], 1: [2, 3], 2: [0, 3], 3: [2]}

print("bfs target=3:", bfs(3, g1))    # True
print("bfs target=9:", bfs(9, g1))    # False
print("dfs target=0:", dfs(0, g1))    # True
print("dfs target=9:", dfs(9, g1))    # False

# DAG for topological sort
edges2 = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
g2 = adjacencySet(edges2)
print("topologicalSort (Kahn's):", topologicalSort(g2))
# One valid order: [4, 5, 2, 0, 3, 1]
print("topologicalSortDfs:", topologicalSortDfs(g2))
# One valid order: [5, 4, 2, 3, 1, 0]

# Edge case: single node
g3 = adjacencySet([])
g3[7] = set()
print("bfs single node, target=7:", bfs(7, g3))   # True
print("bfs single node, target=1:", bfs(1, g3))   # False

# Spent a total of 40 mins on this question
