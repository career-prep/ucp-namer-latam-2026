"""
question:  in unweighted graph (still directed)
- array of pairs of value represent edges
"""

#build graph representation, use an array rather than set.

#return a dict represent adj list:
#key: vertex
#value: the list of its outgoing vertex

"""
idea: 
    create a hashmap represent graph
    loop through every pair:
        loop through every vertex in that pair:
            if the vertex not exist:
                add to hashmap
            else:
                hashmap[pair[0]]=pair[1]
"""

def adjacencyList(edges): 
    graph={}

    #edge case, when the graph is empty 
    if len(edges) == 0:
        return graph

    #loop through every edge
    for edge in edges:
        start_vertex= edge[0]
        end_vertex= edge[1]


        #initialize and assign vertex to "value"
        if start_vertex not in graph:
            graph[start_vertex]=[]
            graph[start_vertex].append(end_vertex)
        else:
            graph[start_vertex].append(end_vertex)
        
        if end_vertex not in graph:
            graph[end_vertex]=[]
        
    return graph


def test1():
    edges= [(1,2), (2,3), (1,3), (3,2), (2,0)]
    print(adjacencyList(edges))




"""
search for a vertex in a graph
ideas:
    use a set to save visited node
    use a queue

    loop through every start vertex, since the graph might not have multiple connected components
        if start vertex visited:
            skip
        
        otherwise, add to the queue
        while the queue is not empty:
            pop the first vertex
            check if vertex= target:
                    yes-> return True

            loop through all the outgoing vertex:
                    if not visited:
                        mark as visited
                        enqueue to the queue and start over
                

"""
from collections import deque

def bfs(target: int, graph) -> bool:

    #track the visited vertex
    visited=set()
    queue=deque()

    #loop through all vertex
    for start_vertex in graph:

        #if start from a visited node -> skip
        if start_vertex in visited:
            continue
        
        #otherwise, add to queue and mark as visited
        queue.append(start_vertex)
        visited.add(start_vertex)

        #bfs
        while queue:
            pop_vertex=queue.popleft()

            #check if its target
            if pop_vertex == target:
                return True
            
            outgoing_vertex= graph[pop_vertex]

            #loop through every neighbor 
            for vertex in outgoing_vertex:
                if vertex in visited:
                    continue
                else:
                    queue.append(vertex)
                    visited.add(vertex)

    return False

#{1: [2, 3], 2: [3, 0], 3: [2], 0: []}

def dfs(target: int, graph) -> bool:
    #mark node when they are visited
    visited = set()

    #helper, node represent the start node
    def dfs_helper(node):
        #base case
        if node == target:
            return True
        
        visited.add(node)

        #discover node using dfs
        for vertex in graph[node]:
            if vertex not in visited:
                if dfs_helper(vertex):
                    return True
        
        return False

    #loop through every node to get the starting node
    for start_vertex in graph:
        if start_vertex not in visited:
            if dfs_helper(start_vertex):
                return True
    
    return False


"""
ideas: using kahn algo
- initilize the in-degree for all node
- init a queue, adding all nodes with 0 in-degree to the queue

- while the queue is not empty:
+   remove a node from queue
+   append it to topo order
+   reduce indegree of its neighbor
+   if any of its neighbor has indegree=0 => add to queue

{1: [2, 3], 2: [3, 0], 3: [2], 0: []}

"""
def topologicalSort(graph): #list of int 
    queue=deque()

    #init the indegree 
    in_degree={}

    #init the indegree for every node=0
    for vertex in graph:
        in_degree[vertex]=0

    #if it have indegree => +=1
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor]+=1
    
    #add all the node with indegree =0
    for in_degree_0_vertex in in_degree:
        if in_degree[in_degree_0_vertex] == 0:
            queue.append(in_degree_0_vertex)
    
    topological_order=[]
    while queue:
        removed_node= queue.popleft()
        topological_order.append(removed_node)

        #reduce in-degree of neighbor
        for neighbor in graph[removed_node]:
            in_degree[neighbor]-=1
        
            if in_degree[neighbor]==0:
                queue.append(neighbor)

    
    return topological_order


"""
ideas:
    track visited node -> use a set
    dfs helper to find the node
    after visiting all adj_node, append to the topo list


"""
def topologicalSortDFS(graph):
    topological_order=[]
    visited=set()

    #helper
    def dfs_helper(node):
        #base case
        if node in visted:
            return 
        
        #mark as visited
        visited.add(node)

        for neighbor in graph[node]:
            dfs_helper(neighbor)
        
        #after exploring every neigbor, add the node
        topological_order.append(node)

    for node in graph:
        if node not in visited:
            dfs_helper(node)

    #reverse since it initally start from the fastest-terminated node
    return topological_order[::-1]



if __name__=="__main__":
    test1()
    print("passed all")


        

       


