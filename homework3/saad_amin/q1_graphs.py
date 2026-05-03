from collections import defaultdict
from collections import deque

def adjacency_set(edges):
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
        
        while queue:
            node = queue.popleft()
            
            if node == target:
                return True
            
            if node not in visited:
                visited.add(node)
                queue.extend(graph[node])
    
    return False

def dfs(target, graph):
    visited = set()
    
    def dfs_helper(node):
        if node == target:
            return True
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True
        
        return False
    
    for node in graph:
        if node not in visited:
            if dfs_helper(node):
                return True
    
    return False


def topo_dfs(graph):
    visited = set()
    stack = []
    
    def dfs_helper(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
        
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs_helper(node)
    
    return stack[::-1]

def topo_kahn(graph):
    indegree = {node: 0 for node in graph}

    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque([node for node in indegree if indegree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return result
