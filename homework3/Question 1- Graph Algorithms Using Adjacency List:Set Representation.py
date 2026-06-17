graph = {}
def adjacency_set(edges):
    for u, v in edges:
        graph[u] = set()
        graph[v] = set()
    
    for u, v in edges:
        graph[u].add(v)
    
    return graph

def bfs(target, adj):
    q = [0]
    visited = set()
    while q:
        node = q.pop(0)

        if node in visited:
            continue
        visited.add(node)

        if node == target:
            return True
        
        for neighbor in adj[node]:
            q.append(neighbor)

    return False

def dfs(target, adj):
    q = [0]
    visited = set()
    while q:
        node = q.pop()

        if node in visited:
            continue
        visited.add(node)

        if node == target:
            return True
        
        for neighbor in adj[node]:
            q.append(neighbor)

    return False

def topologicalSort(graph):
    in_degree = {}
    for u in graph:
        in_degree[u] = 0

    for u, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1
        
    q = [node for node in graph if in_degree[node] == 0]
    result = []

    while q:
        node = q.pop()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0: 
                q.append(neighbor)

    return result

def topologicalSortDfs(graph):
    visited = set()
    result = []
    for node in graph:
        if node not in visited:
            dfs_helper(node, visited, result, graph)
    return result

def dfs_helper(node, visited, result, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_helper(neighbor, visited, result, graph)
    result.append(node)
