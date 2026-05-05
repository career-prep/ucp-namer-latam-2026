# Technique: Graph Representation, Standard Traversals, and Ordering Algorithms
from collections import deque

def adjacencySet(edges): # Time, Space Complexities: O(E + V), O(V + E)
    # 1. Initialize a map to hold the sets of neighbors
    graph = {}
    
    # 2. Iterate through edges to populate the map and identify all nodes
    for u, v in edges:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        
        # 3. Add the directed edge from u to v
        graph[u].add(v)
        
    return graph

def bfs(target, graph): # Time, Space Complexities: O(V + E), O(V)
    if not graph:
        return False
        
    # 1. Use a queue for level-order traversal (FIFO)
    # Start from an arbitrary node (first key in map)
    start_node = next(iter(graph))
    queue = deque([start_node])
    visited = {start_node}
    
    # 2. Process nodes until the queue is empty
    while queue:
        curr = queue.popleft()
        
        if curr == target:
            return True
        
        # 3. Explore neighbors
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def dfs(target, graph): # Time, Space Complexities: O(V + E), O(V)
    visited = set()
    
    # 1. Recursive helper to explore as deep as possible before backtracking
    def search(curr):
        if curr == target:
            return True
        visited.add(curr)
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                if search(neighbor):
                    return True
        return False
    
    # 2. Iterating over all nodes handles disconnected components
    for node in graph:
        if node not in visited:
            if search(node):
                return True
    return False

def topologicalSort(graph): # Technique: Kahn's Algorithm (BFS-based). O(V+E), O(V)
    # 1. Calculate in-degree (number of incoming edges) for all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
            
    # 2. Queue nodes with 0 in-degree (no prerequisites)
    queue = deque([n for n in in_degree if in_degree[n] == 0])
    result = []
    
    # 3. Repeatedly remove nodes with 0 in-degree and update neighbors
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    # 4. If result size < graph size, there is a cycle
    return result if len(result) == len(graph) else []

def topologicalSortDfs(graph): # Technique: DFS Post-Order Stack. O(V+E), O(V)
    visited = set()
    visiting = set() # For cycle detection (Back-edges)
    stack = []
    
    def visit(n):
        if n in visiting: # Cycle detected
            return False
        if n in visited:
            return True
            
        visiting.add(n)
        for neighbor in graph.get(n, []):
            if not visit(neighbor):
                return False
        
        visiting.remove(n)
        visited.add(n)
        # 1. Add to stack only after all descendants are processed
        stack.append(n)
        return True

    for node in graph:
        if node not in visited:
            if not visit(node):
                return []
    
    # 2. The order is the reverse of the finishing times
    return stack[::-1]

class Test:
    def run_tests(self):
        edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
        g = adjacencySet(edges)
        assert bfs(0, g) == True
        assert dfs(99, g) == False
        
        print("All Tests Passed")

if __name__ == "__main__":
    Test().run_tests()
