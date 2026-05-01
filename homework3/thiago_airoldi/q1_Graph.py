from collections import defaultdict
from collections import deque


edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]

def createGraph(edges):

    adjacencyList = defaultdict(list)

    # First Find All vertices (nodes)
    vertices = set()
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)
    

    # Next, initialize all vertices with an empty list
    for v in vertices:
        adjacencyList[v] = []


    # Lastly, add edges
    for u, v in edges:
        adjacencyList[u].append(v)


    return adjacencyList


adj = createGraph(edges)

# Print adjacency list in form "vertex: [neighbors]"
for v in sorted(adj):
    print(f"{v}: {adj[v]}")








# Basic BFS that searches for a target value. Returns a boolean depending on if found or not.
# Time Complexity of O(V + E) where V is the number of nodes and E is the number of edges
# Space Complexity of O(V) (for the seen set that holds all V number of nodes)
def bfs(target, graph):
    
    seen = set()

    for node in graph:
        if node in seen:
            # Skip it
            continue

        q = deque()
        q.append(node)
        seen.add(node)

        while q:

            node = q.popleft()

            if node == target:
                return True
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)


    return False




# Basic DFS that searches for a target value. Returns a boolean depending on if found or not.
# Time Complexity of O(V + E) where V is the number of nodes and E is the number of edges
# Space Complexity of O(V)
def dfs(target, graph):


    # Keep track of nodes we have seen so we do not travel to them again
    seen = set()

    def recursiveDFS(node):
        if node == target:
            return True
        
        if node in seen:
            return False
        
        # Add current node to seen set when we visit it (if we get here, it has not been seen before)
        seen.add(node)

        # Traverse onto this node's neighbors
        for neighbor in graph[node]:
            if recursiveDFS(neighbor) == True:
                # Target is found
                return True
            
        # Target not found
        return False
    

    # Run the DFS
    for node in graph:
        if recursiveDFS(node) == True:
            return True
        
    return False
    


# Topological Sort using Kahn's Algorithm. Returns an integer array
# Repeatedly remove nodes without any dependencies from the graph and add them to the topological ordering
# We repeat removing nodes without dependencies from the graph until all nodes are processed, or a cycle is discovered
# O(V + E) Time Complexity
# O(V) Space Complexity
def topolocigalSort(graph):
    
    # First Compute independence-degree of every node
    inDegree = {}

    for node in graph:
        inDegree[node] = 0 # Initially 0 for every node

    for node in graph:
        for neighbor in graph[node]:
            inDegree[neighbor] += 1


    
    # Next, initialize queue with all nodes that have in-degree of 0
    q = deque()
    for node in graph:
        if inDegree[node] == 0:
            q.append(node)


    topoSort = [] # Stores the topological sort


    # Next, do a BFS, pop from queue and reduce in-degree of all neighbors
    while q:
        node = q.popleft()
        topoSort.append(node)

        for neighbor in graph[node]:
            inDegree[neighbor] -= 1

            # If a neighbor's in-degree now reaches zero, add it to the queue
            if inDegree[neighbor] == 0:
                q.append(neighbor)


    # If we encountered a cycle, topoSort array would not contain all nodes in the graph (if len(topoSort) != len(graph) then cycle detected)

    return topoSort


# Topological Sort using DFS. Returns an integer array.
# O(V + E) Time Complexity, V being number of nodes and E being number of edges in graph
# O(V) Space Complexity, V being number of nodes (O(V) for call stack, for the actual stack, and for the seen set)
def topologicalSortDfs(graph):

    # Helper dfs function that does post-order traversal
    def dfs(graph, node, stack, seen):

        seen.add(node)

        for neighbor in graph[node]:
            if neighbor not in seen:
                dfs(graph, neighbor, stack, seen)

        # After processing all neighbors, append this node to the stack
        stack.append(node)


    stack = [] # Keeps track of nodes in reverse order needed for topological sort

    seen = set()

    # Populate stack
    for node in graph:

        if node not in seen:
            dfs(graph, node, stack, seen)

    topoSort = [] # fill this by popping from the stack until it's empty (basically reversing the ordering in the stack)

    while stack:
        topoSort.append(stack.pop())

    return topoSort




    
