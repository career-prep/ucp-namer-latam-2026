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


def bfs(target, graph):
    if not graph:
        return False

    visited = set()
    for start in graph:
        if start in visited:
            continue

        q = deque([start])
        visited.add(start)

        while q:
            node = q.popleft()

            if node == target:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

    return False


def dfs(target, graph):
    if not graph:
        return False

    visited = set()

    def traverse(node):
        if node == target:
            return True
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if traverse(neighbor):
                    return True
        return False

    for start in graph:
        if start not in visited:
            if traverse(start):
                return True

    return False


def topologicalSort(graph):
    indegree = {}

    for node in graph:
        indegree[node] = 0

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    q = deque()
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return result


def topologicalSortDfs(graph):
    visited = set()
    stack = []

    def dfs_topological_sort(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_topological_sort(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs_topological_sort(node)

    return stack[::-1]
