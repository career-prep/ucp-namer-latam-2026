from collections import deque
def createGraph(edges):
    graph = {}

    for u, v in edges:
        if u not in graph: graph[u] = set()
        if v not in graph: graph[v] = set()
        graph[u].add(v)
    return graph

def bfs(target, graph):
    start = next(iter(graph))
    seen = set([start])
    q = deque([start])

    while q:
        cur = q.popleft()
        if cur == target:
            return True

        for neighbor in graph.get(cur, []):
            if neighbor not in seen:
                seen.add(neighbor)
                q.append(neighbor)
    return False


def dfs(target, graph):
    seen = set()

    def search(cur):
        if cur == target:
            return True
        seen.add(cur)

        for neighbor in graph[cur]:
            if neighbor not in seen:
                if search(neighbor):
                    return True
        return False
    
    for node in graph:
        if node not in seen:
            if search(node):
                return True
    return False


def topologicalSort(graph):
    in_degree = {node: 0 for node in graph} # Count in-degrees (how many nodes point to this node)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
            
    
    queue = deque([n for n in in_degree if in_degree[n] == 0]) # Add nodes with 0 incoming edges to the queue
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        # For each neighbor, decrease an the edge and check in-degree
        for neighbor in graph.get(u, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    return result if len(result) == len(graph) else []

def topologicalSortDfs(graph):
    visited = set()
    stack = []
    
    def visit(node):
        if node in visited:
            return
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            visit(neighbor)
        stack.append(node)

    for node in graph:
        visit(node)
    return stack[::-1]


edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
graph = createGraph(edges)
print(graph)
print(dfs(3, graph))
print(dfs(5, graph))

print(bfs(3, graph))
print(dfs(5, graph))

print(topologicalSort(graph))
print(topologicalSortDfs(graph))

# Graph with a Cycle (3 -> 2 -> 3)
edges_cycle = [(1, 2), (2, 3), (3, 2)]
graph_cycle = createGraph(edges_cycle)
print(graph_cycle)
print(topologicalSort(graph_cycle))
print(topologicalSortDfs(graph_cycle))