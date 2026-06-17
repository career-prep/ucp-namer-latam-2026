from collections import deque, defaultdict

def build_adjacency_set(edges):

    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        if v not in adj:
            adj[v] = set()
    return adj

def bfs(graph, target):
    if not graph:
        return False
    
    start_node = next(iter(graph))
    visited = {start_node}
    queue = deque([start_node])
    
    while queue:
        current = queue.popleft()
        if current == target:
            return True
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def dfs(graph, target):
    if not graph:
        return False
        
    start_node = next(iter(graph))
    visited = set()

    def search(u):
        if u == target:
            return True
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                if search(v):
                    return True
        return False

    return search(start_node)

def topological_sort_kahn(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
            

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(result) != len(graph):
        return "Cycle detected! No valid topological sort."
    return result

def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def visit(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                visit(v)
        stack.append(u)

    for node in graph:
        if node not in visited:
            visit(node)
            
    return stack[::-1]


if __name__ == "__main__":
    example_edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    adj_set = build_adjacency_set(example_edges)
    
    print(f"Adjacency Set: {dict(adj_set)}")
    print(f"BFS target 0: {bfs(adj_set, 0)}")
    print(f"DFS target 3: {dfs(adj_set, 3)}")
    print(f"Kahn's Topo Sort: {topological_sort_kahn(adj_set)}")