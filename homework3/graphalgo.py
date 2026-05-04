# Technique: Adjacency Set (dict of sets) + iterative DFS/BFS + DFS post-order topo + Kahn's BFS topo
# Time Complexity: adjacencySet O(E), dfs/bfs O(V+E), topo sorts O(V+E)
# Space Complexity: O(V+E) for graph storage, O(V) for visited/queue/stack

from collections import deque

def adjacencySet(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
    return graph


def dfs(graph, start, target):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == target:
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                stack.append(neighbor)
    return False


def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
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


# Topo sort via DFS post-order then reverse
# Assumption: graph is a DAG
def topoSortDFS(graph):
    visited = set()
    result = []

    def helper(node):
        visited.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                helper(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            helper(node)

    result.reverse()
    return result


# Topo sort via Kahn's algorithm (BFS on in-degrees)
# Returns [] if cycle detected
def topoSortKahns(graph):
    inDegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in inDegree:
                inDegree[neighbor] = 0
            inDegree[neighbor] += 1

    queue = deque([node for node in inDegree if inDegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, set()):
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(inDegree):
        return []  # cycle exists
    return result


# Test 1: example from assignment
# Input: [(1,2),(2,3),(1,3),(3,2),(2,0)]
edges1 = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
g1 = adjacencySet(edges1)
print(g1)                    # {1:{2,3}, 2:{0,3}, 3:{2}, 0:set()}
print(dfs(g1, 1, 0))         # True
print(dfs(g1, 0, 1))         # False  (0 has no outgoing edges)
print(bfs(g1, 1, 0))         # True
print(bfs(g1, 0, 1))         # False

# Test 2: DAG topo sort
edges2 = [(0, 1), (0, 2), (1, 3), (2, 3)]
g2 = adjacencySet(edges2)
print(topoSortDFS(g2))       # [0, 2, 1, 3] or [0, 1, 2, 3]
print(topoSortKahns(g2))     # [0, 1, 2, 3] or [0, 2, 1, 3]

# Test 3: cycle detection via Kahn's
edges3 = [(0, 1), (1, 2), (2, 0)]
g3 = adjacencySet(edges3)
print(topoSortKahns(g3))     

# Time spent: ~90 minutes