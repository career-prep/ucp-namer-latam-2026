#Graph Algorithm using Adjacency List/Set Representation

from collections import deque

def build_adjacency_set(edges): #use a hash map with nodes as keys and all neighbors in a set as their values
    node_to_neighbors_map = {}
    for source_node, destination_node in edges:
        if source_node not in node_to_neighbors_map:
            node_to_neighbors_map[source_node] = set() #create empty set if node not in the map
        if destination_node not in node_to_neighbors_map:
            node_to_neighbors_map[destination_node] = set()
        node_to_neighbors_map[source_node].add(destination_node)
    
    return node_to_neighbors_map

def dfs(node_to_neighbors_map, start, target):
    visited_nodes = set()

    def dfs_helper(current_node, visited_nodes):
        visited_nodes.add(current_node)

        if current_node == target:
            return True
        
        for neighboring_node in node_to_neighbors_map[current_node]:
            if neighboring_node not in visited_nodes:
                if dfs_helper(neighboring_node, visited_nodes):
                    return True
                
        return False
    
    return dfs_helper(start, visited_nodes)
        

def bfs(node_to_neighbors_map, start, target):
    visited_nodes = set([start])
    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        if current_node == target:
            return True
        
        for neighboring_node in node_to_neighbors_map[current_node]:
            if neighboring_node not in visited_nodes:
                visited_nodes.add(neighboring_node)
                queue.append(neighboring_node)
    

    return False

def topological_sort_dfs(node_to_neighbors_map): #Assumption: No cycles in Graph
    visited_nodes = set()
    result = []

    for graph_node in node_to_neighbors_map:
        if graph_node not in visited_nodes:
            dfs_recursive_helper(graph_node)


    def dfs_recursive_helper(current_node):
        visited_nodes.add(current_node)
        for neighboring_node in node_to_neighbors_map[current_node]:
            if neighboring_node not in visited_nodes:
                dfs_recursive_helper(neighboring_node)

        result.append(current_node)

    
    return result[::-1]

    
def topological_sort_bfs(node_to_neighbors_map):
    node_to_dependencyCount_map = {}
    for node in node_to_neighbors_map:
        node_to_dependencyCount_map[node] = 0

    for source_node in node_to_neighbors_map:
        for destination_node in node_to_neighbors_map[source_node]:
            node_to_dependencyCount_map[destination_node] += 1
    
    zero_dependency_node_queue = deque()
    for node in node_to_dependencyCount_map:
        if node_to_dependencyCount_map[node] == 0:
            zero_dependency_node_queue.append(node)
    
    result = 0

    while zero_dependency_node_queue:
        current_node = zero_dependency_node_queue.popleft()
        result.append(current_node)

        for neighboring_node in node_to_neighbors_map[current_node]:
            node_to_dependencyCount_map[neighboring_node] -= 1
            if node_to_dependencyCount_map[neighboring_node] == 0:
                zero_dependency_node_queue.append(neighboring_node)

    if len(result) != len(node_to_neighbors_map):
        raise Exception("Cycle Detected.")
    
    return result

    