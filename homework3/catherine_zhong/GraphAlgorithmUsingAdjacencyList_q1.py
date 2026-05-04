from collections import deque

def adjacencySet(edges):
    graph = dict()

    for a, b in edges:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b] = []

    return graph

#runtime: O(V+E)
def bfs(target, graph):
    q = deque()
    visited = set()

    for start in graph:
        if start in visited:
            continue

        q.append(start)
        visited.add(start)

        while q:
            node = q.popleft()

            if node == target:
                return True

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)

    return False

#runtime: O(V+E)
def dfs(target, graph):
    visited = set()

    def explore(node):
        if node == target:
            return True

        visited.add(node)

        for i in graph[node]:
            if i not in visited:
                if explore(i):
                    return True
        return False

    for i in graph:
        if i not in visited:
            if explore(i):
                return True

    return False

#runtime: O(V+E)
def topologicalSort(graph):
    degree = {i:0 for i in graph}
    for i in graph:
        for j in graph[i]:
            degree[j] += 1
    q = deque([i for i in degree if degree[i] == 0])
    order = []

    while q:
        top = q.popleft()
        order.append(top)

        for i in graph[top]:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)

    if len(order) != len(degree):
        return []

    return order

#runtime: O(V+E)
def topologicalSortDfs(graph):
    visited = set()
    visiting = set()

    stack = []
    def explore(node):
        if node in visiting:
            return False
        if node in visited:
            return True

        visiting.add(node)

        for i in graph[node]:
            if not explore(i):
                return False

        visiting.remove(node)
        visited.add(node)
        stack.append(node)

        return True

    for i in graph:
        if i not in visited:
            if not explore(i):
                return []
        
    return stack[::-1]

#test cases for adjacencySet
input = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
graph = adjacencySet(input)
print(f"adjacency list: {graph}")

#test bfs
print('\nbfs tests')
print(f'contains 2: {bfs(2, graph)}')
print(f'contains 4: {bfs(4, graph)}')

#test cases for dfs
print('\ndfs tests')
print(f'contains 3: {dfs(3, graph)}')
print(f'contains 5: {dfs(5, graph)}')

#test cases for khans's topological sort
graph2 = {5: [2], 4: [1], 2: [3], 3: [1], 1: []}
print('\ntopological sort using Khans')
print(f'graph with cycle: {topologicalSort(graph)}')
print(f'graph with no cycles: {topologicalSort(graph2)}')

#test cases for dfs topological sort
print('\ndfs topological sort tests')
print(f'graph with cycle: {topologicalSortDfs(graph)}')
print(f'graph with no cycles: {topologicalSortDfs(graph2)}')

#time spent: 40 min