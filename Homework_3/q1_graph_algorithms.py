# Given an array of pairs of values representing edges in an unweighted undirected_graph,
# create the equivalent adjacency list/set representation
# (a map from element to a list or set of elements).
#
# Pairs represent directed edges: (A, B) means there is an edge from A to B.
# If the pair (B, A) is also provided, then there is an undirected edge between A and B.
#
# For simplicity, you may assume that each node of the undirected_graph stores an integer
# rather than a generic data type and that the elements are distinct.
#
# Implement:
#   1. Basic DFS that searches for a target value
#   2. Basic BFS that searches for a target value
#   3. Topological sort using DFS
#   4. Topological sort using Kahn's algorithm (BFS-based)

from collections import defaultdict,deque

#Cyclic pairs
pairs = [
    (1, 2), (2, 1), 
    (1, 3), (3, 1), 
    (2, 4), (4, 2), 
    (3, 4), (4, 3), 
]
#Undirected graph
def adjacency_set(arr):
    graph=defaultdict(set)
    for u,v in arr:
        graph[u].add(v)
        graph[v].add(u)
    return graph
undirected_graph=adjacency_set(pairs)

#Acyclic pairs
acyclic_pairs = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
]

#Directed graph for topological sort 
def adjacency_set_top(arr):
    directed_graph=defaultdict(set)
    for u,v in arr:
        directed_graph[u].add(v)
    return directed_graph
directed_graph=adjacency_set_top(acyclic_pairs)

#Time Complexity: O(E)
#Space Complexity: O(V+E)


def dfs_search(undirected_graph,start,visited,target):
    if start==target:
        return True
    visited.add(start)
    for nei in undirected_graph[start]:
        if nei not in visited:
            if dfs_search(undirected_graph,nei,visited,target):
                return True
    return False


#Time Complexity: O(V+E)
#Space Complexity: O(V)

print(dfs_search(undirected_graph, 1, set(), 4))  
print(dfs_search(undirected_graph, 1, set(), 3))  
print(dfs_search(undirected_graph, 1, set(), 5)) 
print(dfs_search(undirected_graph, 2, set(), 3)) 
print(dfs_search(undirected_graph, 4, set(), 4)) 


def bfs_search(undirected_graph,start,target):
    visited=set()
    queue=deque([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        if node==target:
            return True
        for nei in undirected_graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return False

#Time Complexity: O(V+E)
#Space Complexity: O(V)

print(bfs_search(undirected_graph, 1, 4))  
print(bfs_search(undirected_graph, 1, 3))  
print(bfs_search(undirected_graph, 1, 5)) 
print(bfs_search(undirected_graph, 2, 3)) 
print(bfs_search(undirected_graph, 4, 4))



def dfs_sort(graph):
    visited=set()
    result=[]
    def dfs(start):
        visited.add(start)
        for nei in graph[start]:
            if nei not in visited:
                dfs(nei)
        result.append(start)

    for nei in list(graph):
        if nei not in visited:
            dfs(nei)
    return result[::-1]

print(dfs_sort(directed_graph))

#Time Complexity: O(V+E)
#Space Complexity: O(V)


def bfs_sort(graph):
    #Finding degree of connections for each node
    connections = {node: 0 for node in graph}
    for node in graph:
        for nei in graph[node]:
            connections[nei]+=1
    #BFS
    queue=deque(node for node in graph if connections[node]==0)
    result=[]
    while queue:
        node=queue.popleft()
        result.append(node)
        for nei in graph[node]:
            connections[nei]-=1
            if connections[nei]==0:
                queue.append(nei)
    return result

print(bfs_sort(directed_graph))
    

#Time Complexity: O(V+E)
#Space Complexity: O(V)


#Spent a total of 2 hours