from collections import deque

# O(V + E) time and space for all the traversals here

# Input: [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
# Output:
# {
#    0: []
#    1: [2, 3]
#    2: [0, 3]
#    3: [2]
#}


def adjacencySet(edges): # This took me 10 minutes
    graph = {}

    for source, destination  in edges:
        if source not in graph:
            graph[source] = set([])
        if destination not in graph:
            graph[destination] = set([])

        graph[source].add(destination)

    return graph

test1 = adjacencySet([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])

print(test1)


def dfs(target, graph): # This took me ~15 minutes
    
    visited = set()

    def dfs_helper(node):

        if node == target:
            return True 

        visited.add(node)
        
        for dest in graph[node]:
            if dest not in visited:
                found_target = dfs_helper(dest)
                if found_target:
                    return True 

        return False

    for initial_node in graph: # for loop finds disconnected nodes
        if initial_node not in visited:
            found_target2 = dfs_helper(initial_node)
            if found_target2:
                return True 
        
    return False
    
test2 = dfs(4, test1)
print(test2)

def bfs(target, graph): # This took me ~20 minutes
    visited = set()

    for node in graph:
        if node in visited:
            continue        # For loop to get disconnected nodes. Skip (continute) if seen already.
        queue = deque([node])
        visited.add(node)

        while queue:
            top = queue.popleft()
            
            if top == target:
                return True 

            for destination in graph[top]:
                if destination not in visited:
                    queue.append(destination)
                    visited.add(destination)

    return False
    
test2 = bfs(2,test1)
print(test2)

def top_dfs(graph): # this took me 50 minutes. Top sort feels like unfamiliar territory and had a hard time with this. 
    visited = set()
    top_list = []
    def top_dfs_helper(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                top_dfs_helper(neighbor)
        top_list.append(node)
        
    for node in graph:
        if node not in visited:
            top_dfs_helper(node)

    return top_list[::-1]

test3 = top_dfs(adjacencySet([(1,2),(2,3),(3,4),(4,5)]))
print(test3)

test3 = top_dfs(adjacencySet([(1,2),(1,3),(3,4),(4,5)]))
print(test3)

def top_khan(graph): # This took me ~40 minutes. Felt a lot more straight forward than the DFS approach.

    # Start by counting edges
    # Make a queue of nodes with zero dependencies
    # Pop the nodes from the queue and remove one dependency from it's neighbors
    # If the dependency count = 0, add to queue. No need to recalculate previous steps
    
    result = []
    count = {}
    for node in graph:
        count[node] = 0

    for node in graph:
        for neighbor in graph[node]:
            count[neighbor] += 1 

    queue = deque()
    
    for node in graph:
        if count[node] == 0:
            queue.append(node)

    while queue:
        current_node = queue.popleft()
        result.append(current_node)
        for neighbor in graph[current_node]: # after building the initial queue 
            count[neighbor] -= 1             # we can avoid recalculating from the graph
                                             # by appending the neighbors as they hit 0 
            if count[neighbor]== 0:
                queue.append(neighbor)

    return result

test4 = top_khan(adjacencySet([(1,2),(2,3),(3,4),(4,5)]))
print(test4)

test4 = top_khan(adjacencySet([(1,2),(1,3),(3,4),(4,5)]))
print(test4)


