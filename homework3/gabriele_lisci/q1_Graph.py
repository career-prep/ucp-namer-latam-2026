"""
Graph Methods

createGraph(pairs)
    Time: O(n)
    Space: O(V+E)

dfs(target, graph)
    Time: O(V+E)
    Space: O(V)

bfs(target, graph)
    Time: O(V+E)
    Space: O(V)

topologicalSort(graph)
    Time: O(V+E)
    Space: O(V)

topologicalSortdfs(graph)
    Time: O(V+E)
    Space: O(V)
"""

import collections
def createGraph(pairs):
    graph = collections.defaultdict(list)
    for v1, v2 in pairs:
        graph[v1].append(v2)
        if v2 not in graph:
            graph[v2] = []
    return graph

def printGraph(graph):
    for key,val in graph.items():
        print(str(key) + " : " + str(val))


def dfs(target, graph):
    if not graph:
        return False
    def helper(node, graph, visited):
        if node == target:
            return True
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                helper(nei, graph, visited)
        return False


    visited = set()
    for node in graph.keys():
        if node not in visited:
            if helper(node, graph, visited):
                return True
    return False



def bfs(target, graph):
    if not graph:
        return False
    def helper(node, graph, visited):
        q = collections.deque()
        q.append(node)
        visited.add(node)
        while q:
            curr = q.popleft()
            if curr == target:
                return True
            for nei in graph[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        return False

    visited = set()
    for node in graph:
        if node not in visited:
            if helper(node, graph, visited):
                return True
    return False

# Assumption: no cycle in graph
def topologicalSort(graph):
    if not graph:
        return []
    res = []
    indegrees = {}
    for key in graph.keys():
        indegrees[key] = 0

    for nodes in graph.values():
        for node in nodes:
            indegrees[node] += 1

    q = collections.deque()
    for key, value in indegrees.items():
        if value == 0:
            q.append(key)
    while q:
        curr = q.popleft()
        res.append(curr)
        for node in graph[curr]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                q.append(node)
    return res

# Assumption: no cycle in graph
def topologicalSortdfs(graph):
    if not graph:
        return []
    def dfs(node, visited, stack):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, visited, stack)
        stack.append(node)
    stack = []
    visited = set()
    for node in graph.keys():
        if node not in visited:
            dfs(node, visited, stack)
    return stack[::-1]




graph = createGraph([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])
printGraph(graph)


# target is in graph
print(dfs(3, graph) == True)
# target is not in graph
print(dfs(4, graph) == False)
# empty graph
print(dfs(3, None) == False)


# target is in graph
print(bfs(3, graph) == True)
# target is not in graph
print(bfs(4, graph) == False)
# empty graph
print(bfs(3, None) == False)

graph = createGraph([(1, 2), (2, 3), (1, 3), (2, 0)])
print(topologicalSort(graph))
print(topologicalSort(None))
print(topologicalSortdfs(graph))
print(topologicalSortdfs(None))

# Time Spent: 1:00
