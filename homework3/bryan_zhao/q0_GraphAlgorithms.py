from collections import defaultdict
from collections import deque

def adjacency_set(edges):
    adj_set = defaultdict(set)

    for u, v in edges:
        adj_set[u].add(v)
        if v not in adj_set:
            adj_set[v] = set()

    return adj_set

edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
graph = adjacency_set(edges)
print(graph)

def bfs(target, graph):
    seen = set()

    for node in graph:
        if node not in seen:
            queue = deque([node])
            seen.add(node)

            while queue:
                curr = queue.popleft()
                if curr == target:
                    return True

                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
    
    return False

def dfs(target, graph):
    seen = set()

    def dfs_helper(curr):
        if curr == target:
            return True

        seen.add(curr)

        for neighbor in graph[curr]:
            if neighbor not in seen:
                if dfs_helper(neighbor):
                    return True
        return False
    
    for node in graph:
        if node not in seen:
            if dfs_helper(node):
                return True
            
    return False

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}

    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topological_order = []

    while queue:
        u = queue.popleft()
        topological_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topological_order) == len(graph):
        return topological_order
    else:
        return []
    
def topological_sort_dfs(graph):
    seen = set()
    stack = []

    def dfs(u):
        if u in seen:
            return True
        
        for v in graph[u]:
            if not dfs[v]:
                return False
        
        seen.add(u)
        stack.append(u)
        return True

    for node in list(graph.keys()):
        if node not in seen:
            if not dfs(node):
                return []
            
    return stack[::-1]