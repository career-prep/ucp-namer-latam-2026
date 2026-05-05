def adjacencySet(edges):
    
    graph = {}

    for i, j in edges:

        if i not in graph:
            graph[i] = set()
        graph[i].add(j)

        if j not in graph:
            graph[j] = set()

    return graph 

# edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
# output = {1: {2, 3}, 2: {0, 3}, 3: {2}, 0: set()}

# edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
# output = {0: {1, 2}, 1: {3}, 2: {3}, 3: {4}, 4: set()}
# print(adjacencySet(edges))

from collections import deque

def bfs(target, graph):

    visited = set()
    
    for start in graph:
        if start not in visited:
            queue = deque([start])

            while queue:
                node = queue.popleft()

                if node == target:
                    return True
                
                if node in visited:
                    continue
            
            visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False

# graph = {1: {2, 3}, 2: {0, 3}, 3: {2}, 0: set()}
# target = 3
# Output: True

# graph = {1: {2, 3}, 2: {0, 3}, 3: {2}, 0: set()}
# target = 4
# Output: False
# print(bfs(target, graph))

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
    
    for node in graph:
        if node not in visited:
            if helper(node):
                return True
    return False

# graph = {1: {2, 3}, 2: {0, 3}, 3: {2}, 0: set()}
# target = 3
# Output: True

# graph = {1: {2, 3}, 2: {0, 3}, 3: {2}, 0: set()}
# target = 4
# Output: False
# print(dfs(target, graph))

def topsort(graph):

    indegree = {}

    for node in graph:
        indegree[node] = 0

    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    res = []

    queue = deque()

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)
    
    while queue:
        node = queue.popleft()
        res.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return res

# single starter
# graph = {
#     1: {2},
#     2: {3},
#     3: set()
# }
# output: [1, 2, 3]

# multiple starter
# graph = {
#     5: {2, 0},
#     4: {0, 1},
#     2: {3},
#     3: {1},
#     1: set(),
#     0: set()
# }
# possible output: [5, 4, 2, 0, 3, 1] 

# print(topsort(graph))

def topsort_dfs(graph):

    visited = set()
    res = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        res.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)
    
    res = res[::-1]
    return res

# single starter
# graph = {
#     1: {2},
#     2: {3},
#     3: set()
# }
# output: [1, 2, 3]

# multiple starter
# graph = {
#     5: {2, 0},
#     4: {0, 1},
#     2: {3},
#     3: {1},
#     1: set(),
#     0: set()
# }
# possible output: [5, 4, 2, 0, 3, 1] 

# print(topsort_dfs(graph))    

# 1hr 40