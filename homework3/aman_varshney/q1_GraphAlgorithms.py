from typing import Tuple 
from collections import deque

class GraphAlgos:
    def __init__(self) -> None:
        pass
    
    def adjacency_set(self, edges: [Tuple]) -> dict[int, set[int]]:
        """Inputs a list of directed edges. Outputs an adjacency set"""
        adj_set = {} # node : [neighbors]
        for src, dest in edges:
            # add vertice
            if src in adj_set:
                adj_set[src].add(dest)
            else:
                adj_set[src] = {dest}
            
            # add edge 2 as empty
            if dest not in adj_set:
                adj_set[dest] = set()
                
        return adj_set
            
    
    def test_adj_set(self, edges: [Tuple]) -> None:
        """Prints adjacency set"""
        adj_set = self.adjacency_set(edges)
        for node in sorted(adj_set):
            print(f"{node}: {sorted(adj_set[node])}")
            
            
            
    def bfs(self, target: int, graph: dict[int, set[int]]) -> bool:
        """Searches for a path to `target` in `graph` starting from 0 using bfs. Returns true if found; else false."""  
        if 0 not in graph: # no path because no mapping to or from 0 in graph
            return False
        
        visited = set([0])
        queue = deque([0]) # start with 0 
        
        while queue: 
            node = queue.popleft()
            if node == target: # found
                return True
            
            # enqueue adjacency list
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return False
        
        
    def dfs(self, target: int, graph: dict[int, set[int]]) -> bool:
        """Searches for a path to `target` in `graph` starting from 0 using dfs. Returns true if found; else false."""
        if 0 not in graph: # no path because no mapping to or from 0 in graph
            return False
        
        def dfs_helper(node):
            """Helper to iterate through neighbors for a node"""
            if node == target: # found
                return True
            visited.add(node)
            
            for neighbor in graph[node]: # check neighbors for new paths
                if neighbor not in visited: 
                    if dfs_helper(neighbor):
                        return True
                    
            return False
        
        
        visited = set()
        return dfs_helper(0) # start with 0 
    
        
    def top_sort(self, graph: dict[int, set[int]]) -> list[int]:
        """Performs topological sort on `graph` using Kahn's."""
        # calculate in degree of each node
        indegree = {node: 0 for node in graph} # node : indegree value
        for key in graph: # iterate through each adjacency set
            for node in graph[key]:
                indegree[node] += 1
                    
        # enqueue nodes with indegree = 0 
        queue = deque()
        for node in graph:
            if indegree[node] == 0:
                queue.append(node) 
        
        # kahns algo
        top_sorted = []
        while queue:
            # move node to result list
            node = queue.popleft()
            top_sorted.append(node) 
            
            for adj_node in graph[node]: # decrement indegree of each adjacency node
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0: # enqueue if indegree is 0 now
                    queue.append(adj_node)
                    
        if len(top_sorted) != len(graph): # cycle
            return []
        return top_sorted
        
        
    def top_sort_dfs(self, graph: dict[int, set[int]]) -> list[int]:
        """Performs topological sort on `graph` using dfs."""
        visited = set()
        cycle_set = set() # used to track cycle
        res = []
        
        def top_dfs_helper(node):
            """Helper to iterate through neighbors and append node."""
            if node in cycle_set: # cycle
                return True
            if node in visited: # already accounted for
                return False
            
            cycle_set.add(node) # add to cycle check
            for neighbor in graph[node]: # check neighbors 
                if neighbor not in visited:
                    if top_dfs_helper(neighbor):
                        return True
            
            res.append(node) # append original after exploring neighbors
            cycle_set.remove(node)
            visited.add(node)
            return False
        
            
        for node in graph: # verifies every node accounted for
            if node not in visited:
                if top_dfs_helper(node): # cycle
                    return []

        return res[::-1] # reverse list
        
        
        
if __name__ == '__main__':
    # init
    ga = GraphAlgos()
    arr1 = [(1,2), (2,3), (1, 3), (3, 2), (2, 0)]
    graph = ga.adjacency_set(arr1)
    
    # adjacency set
    print(" -- Adjacency set test -- ")
    print("Input: [(1,2), (2,3), (1, 3), (3, 2), (2, 0)]")
    print("Expected:")
    print("0: []")
    print("1: [2, 3]")
    print("2: [0, 3]")
    print("3: [2]")
    print("Actual:")
    ga.test_adj_set(arr1)
    
    # bfs/dfs 
    print("-- BFS/DFS test --")
    print("Input = 10")
    print("Expected: False")
    print("Actual (bfs):", ga.bfs(10, graph))
    print("Actual (dfs):", ga.dfs(10, graph))
    print("Input = 0")
    print("Expected: True")
    print("Actual (bfs):", ga.bfs(0, graph))
    print("Actual (dfs):", ga.dfs(0, graph))
    
    # top sort
    print("-- Topological sort test --")
    print("Input: [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]")
    print("Expected output: []") # cycle
    print("Actual output (kahn):", ga.top_sort(graph))
    print("Actual output (dfs):", ga.top_sort_dfs(graph))
    
    arr2 = [(0, 1), (4, 5), (5, 1), (1, 2), (5, 2), (2, 3)]
    graph2 = ga.adjacency_set(arr2)
    print("Input: [(0, 1), (4, 5), (5, 1), (1, 2), (5, 2), (2, 3)]")
    print("Expected output: [0, 4, 5, 1, 2, 3] (not unique)")
    print("Actual output (kahn):", ga.top_sort(graph2))
    print("Actual output (dfs):", ga.top_sort_dfs(graph2))
    
    