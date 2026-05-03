from collections import deque

def build_graph(edges = None):
    if edges:
        adjacencySet = {}
        for u, v in edges:
            if u not in adjacencySet: adjacencySet[u] = set()
            if v not in adjacencySet: adjacencySet[v] = set()
            adjacencySet[u].add(v)
        return adjacencySet

    edges = []
    while True:
        user_input = input("Enter a space separated edge or q to quit: ")
        if user_input.lower() == "q":
            break
        
        try:
            u, v = map(int, user_input.split())
            edges.append((u, v))
        except ValueError:
            print("Invalid input. Please enter two integers (e.g., 1 2).")

    adjacencySet = {}
    for u, v in edges:
        if u not in adjacencySet: adjacencySet[u] = set()
        if v not in adjacencySet: adjacencySet[v] = set()
        adjacencySet[u].add(v)

    return adjacencySet

# take adjacency list, return bfs
def bfs_traversal(graph):
    visited = set()
    res = []

    for start in graph:
        if start not in visited:
            q = deque([start])
            visited.add(start)

            while q:
                curr = q.popleft()
                res.append(curr)

                for neighbor in graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
    return res

# take target val + adjacency list, return bool
def bfs(target, graph):
    visited = set()
    res = []

    for start in graph:
        if start not in visited:
            q = deque([start])
            visited.add(start)

            while q:
                curr = q.popleft()
                if curr == target:
                    return True
                res.append(curr)

                for neighbor in graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
    
    return False

def dfs_traversal_recurse(graph, visited, curr, res):
    visited.add(curr)
    res.append(curr)

    for neighbor in graph.get(curr, []):
        if neighbor not in visited:
            dfs_traversal_recurse(graph, visited, neighbor, res)

# take adjacency list, return bfs
def dfs_traversal(graph):
    visited = set()
    res = []

    for start in graph:
        if start not in visited:
            dfs_traversal_recurse(graph, visited, start, res)

    return res

def dfs_recurse(graph, visited, curr, target):
    if curr == target:
        return True
    
    visited.add(curr)

    for neighbor in graph.get(curr, []):
        if neighbor not in visited:
            if dfs_recurse(graph, visited, neighbor, target):
                return True
            
    return False

# take target val + adjacency list, return bool
def dfs(target, graph):
    visited = set()

    for start in graph:
        if start not in visited:
            if dfs_recurse(graph, visited, start, target):
                return True

    return False

# take adjacency list, return int array
def topologicalSort(graph):
    res = []
    indegrees = {}
    q = deque()

    for node in graph:
        indegrees[node] = 0

    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] = indegrees.get(neighbor, 0) + 1
    
    for node, indegree in indegrees.items():
        if indegree == 0:
            q.append(node)

    while q:
        curr = q.popleft()
        res.append(curr)

        for neighbor in graph.get(curr, []):
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                q.append(neighbor)

    if len(res) != len(graph):
        print("\tCycle detected!")
        return None
    
    return res

# take adjacency list, return int array
def topologicalSortDfs(graph):
    visited = set()
    visiting = set()
    res = []

    def dfs(node):
        if node in visiting:
            return False

        if node in visited:
            return True

        visiting.add(node)

        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False

        visiting.remove(node)
        visited.add(node)
        res.append(node)   
        return True

    for node in graph:
        if node not in visited:
            if not dfs(node):
                print("\tCycle detected!")
                return []
            
    res.reverse()
    return res


if __name__ == "__main__":
    edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    graph = build_graph(edges)
    print(f"Graph: \n{graph}\n")

    print(f"BFS: {bfs_traversal(graph)}")
    print(f"BFS search for {0}: {bfs(0, graph)}")
    print(f"BFS search for {5}: {bfs(5, graph)}")

    print()

    print(f"DFS: {dfs_traversal(graph)}")
    print(f"DFS search for {0}: {dfs(0, graph)}")
    print(f"DFS search for {5}: {dfs(5, graph)}")

    print()

    print("BFS topological sort:")
    print(f"\t{topologicalSort(graph)}")

    print()

    print("DFS topological sort:")
    print(f"\t{topologicalSortDfs(graph)}")

    print()

    edges = [(1, 2), (2, 3), (1, 3), (2, 0)]
    graph = build_graph(edges)
    print(f"Graph: \n{graph}\n")

    print("BFS topological sort:")
    print(f"\t{topologicalSort(graph)}")

    print()

    print("DFS topological sort:")
    print(f"\t{topologicalSortDfs(graph)}")