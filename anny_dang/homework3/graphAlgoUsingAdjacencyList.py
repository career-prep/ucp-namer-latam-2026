from collections import defaultdict, deque
def adjacencySet(edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        if v not in graph:
            graph[v] = set()
    
    return graph

def indegreeMap(graph):
    """
    Time complexity: O(V + E)
    Space complexity: O(V)
    """
    indegree = {node: 0 for node in graph}

    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    return indegree

def bfs(target, graph):
    """
    idea:
    start with each node in graph and apply bfs traversal for each one by queue
    (we sort graph to make sure we walk through each element in order)
    we keep going until finding that target -> return True
    otherwise, return False

    Time complexity: O(VlogV + ElogV)
    Space complexity: O(V + E)
    """
    visited = set()

    for start in sorted(graph):
        if start in visited:
            continue

        queue = deque([start])

        while queue:
            cur = queue.popleft()
            if cur == target:
                return True
            if cur in visited:
                continue
            visited.add(cur)

            for nei in sorted(graph[cur]):
                if nei in visited:
                    continue
                queue.append(nei)

    return False

def dfs(target, graph):
    """
    idea:
    walk through each node in graph and start from there to traverse deeply each node
    by stack 
    we keep going until finding that target -> return True
    otherwise, return False

    Time complexity: O(VlogV + ElogV)
    Space complexity: O(V + E)
    """
    visited = set()

    for start in sorted(graph):
        if start in visited:
            continue

        stack = [start]

        while stack:
            cur = stack.pop()
            if cur == target:
                return True
            if cur in visited:
                continue
            visited.add(cur)
            
            for nei in sorted(graph[cur]):
                if nei not in visited:
                    stack.append(nei)
    
    return False 

def topologicalSort(graph):
    """
    idea:
    start with nodes with indegree == 0 and put those into a queue 
    use queue to process each node in order
        keep popping element out the queue while adding new element into queue if 
        its indegree = 0
        each time visiting neighbors of a node - decrease its indegree by 1
    then check if len(output) is equal to len(number of nodes) 
        if unequal -> there is cycle -> return None
        else -> return output
    
    Time complexity: O(V + E) (indegreeMap function) + O(V) + O(VlogV) (for loop + sorting)
    + O(ElogV) (pop node out queue and visit each neighbors)
    Space complexity: O(V)
    """
    indegree = indegreeMap(graph)
    queue = deque()

    for node in sorted(indegree):
        if indegree[node] == 0:
            queue.append(node)
    
    output = []

    while queue:
        cur = queue.popleft()
        output.append(cur)

        for nei in sorted(graph[cur]):
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    if len(output) != len(indegree):
        return None

    return output

def topologicalSortDfsRecursion(graph):
    """
    idea:
    use visited, and visiting set to check if there is a cycle
    start with every node in graph (if that node is not visited yet)
    for each node:
        if node in visiting -> we are using that node and now we meet this node again -> cycle -> return False
        if node in visited -> we met this node already, so we dont need to keep going -> return True
        else:
            add this node into visiting 
            visit all its neighbors and dfs that node to go all the way 
            after done visiting 
                remove that node from visiting 
                add that node into visited
                add that node into output
    return reversion of output 

    Time complexity: O(VlogV + ElogV)
    Space complexity: O(V)
    """
    visited, visiting = set(), set()
    output = []

    def dfs(node):
        if node in visiting:
            return False
        if node in visited:
            return True
        
        visiting.add(node)

        for nei in sorted(graph[node]):
            if not dfs(nei):
                return False
        
        visiting.remove(node)
        visited.add(node)
        output.append(node)
        return True
    
    for node in sorted(graph):
        if node not in visited:
            if not dfs(node):
                return None
    
    output.reverse()
    return output

    

ex1 = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
graph1 = adjacencySet(ex1)
print(bfs(2, graph1))
print(dfs(2, graph1))
print(topologicalSort(graph1))
print(topologicalSortDfsRecursion(graph1)) 

ex2 = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
graph2 = adjacencySet(ex2)
print(bfs(5, graph2))
print(dfs(5, graph2))
print(topologicalSort(graph2))
print(topologicalSortDfsRecursion(graph2))
