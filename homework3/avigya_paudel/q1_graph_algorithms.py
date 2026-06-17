from collections import defaultdict, deque

# Total Time taken: 1 hour 3 minutes

def adjacency_set(arr):
    def adjacency_set(arr):
        """
        Build an adjacency map from a list of directed edge pairs.

        Each (u, v) adds v to adj[u]. Nodes that only appear as a
        destination still get an empty list, so every node is a key.
        """
        adj_list = defaultdict[int, list](list)
        for v,e in arr:
            adj_list[v].append(e)
            if e not in adj_list:
                adj_list[e] = []
        return adj_list


def dfs(target: int, graph: dict[int, list]):
    """Return True if `target` is reachable from any node, via DFS."""
    visited = set()
    found = False
    
    def visit(node):
        nonlocal found
        if node in visited: return
        visited.add(node)

        if node == target:
            found = True
            return
        for e in graph[node]:
            visit(e)
        return

    for v, e in graph.items():
        if found: break
        visit(v)

    return found

def bfs(target: int, graph: dict[int, list]):
    """Return True if `target` is reachable from any node, via BFS."""
    q = deque(graph.keys())
    visited = set()
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)

        if node == target: return True

        for e in graph[node]:
            q.append(e)
    return False

def topological_sort_kahn(graph):
    """Topological sort via Kahn's algorithm (BFS on in-degrees).

    Returns nodes in topological order, or [] if `graph` has a cycle.
    Node IDs must be 0..N-1 (in-degrees stored in a list).
    """
    q = deque()
    in_degree = [0]*len(graph)
    res = []

    for v, edges in graph.items():
        for e in edges:
            in_degree[e] += 1
    
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        res.append(node) 

        for e in graph[node]:
            in_degree[e] -= 1
            if in_degree[e] == 0:
                q.append(e) 
    return [] if len(res) != len(graph) else res

def topological_sort_dfs(graph):
    """
    Topological sort via DFS.

    Returns nodes in topological order, or [] if `graph` has a cycle.
    Node IDs must be 0..N-1 (state stored in lists).
    """
    visited = [False]*len(graph)
    visiting = [False]*len(graph)
    is_cycle = False
    
    stack = []

    def sort_dfs(node):
        nonlocal is_cycle
        if visited[node] == True:
            return
        if visiting[node] == True:
            is_cycle = True
            return
        visiting[node] = True 
        for e in graph[node]:
            if visited[e]:
                continue 
            if visiting[e]:
                is_cycle = True
            sort_dfs(e)
        stack.append(node)
        visited[node] = True
        visiting[node] = False
        return 

    for v in graph:
        sort_dfs(v)
    stack.reverse()
    return stack if not is_cycle else []


if __name__ == "__main__":
    arr = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    graph = adjacency_set(arr)
    
    test_dfs_0 = dfs(-1, graph) # expected: False
    test_dfs_1 = dfs(0, graph) # expected: True
    print("Test DFS 0: ",test_dfs_0) # expected: False
    print("Test DFS 1: ",test_dfs_1) # expected: True

    test_bfs_0 = bfs(-1, graph) # expected: False
    test_bfs_1 = bfs(0, graph) # expected: True
    print("TEST BFS 0", test_bfs_0) # expected: False
    print("TEST BFS 1", test_bfs_1) # expected: True

    non_cycle_arr = [(4,2), (3,2), (2,1), (0,1)]
    non_cycle_graph = adjacency_set(non_cycle_arr)
    print("Non Cycle Graph:", non_cycle_graph)
    
    top_dfs_res_0 = topological_sort_dfs(non_cycle_graph)  
    print("TOPOLOGICAL SORT DFS NO CYCLE: ", top_dfs_res_0)

    top_dfs_res_1 = topological_sort_dfs(graph)  
    print("TOPOLOGICAL SORT DFS CYCLE: ", top_dfs_res_1)

    top_kahn_res_0 = topological_sort_kahn(non_cycle_graph) 
    print("TOPOLOGICAL SORT KAHN NO CYCLE: ", top_kahn_res_0)

    top_kahn_res_1 = topological_sort_kahn(graph) 
    print("TOPOLOGICAL SORT KAHN CYCLE: ", top_kahn_res_1)

    

