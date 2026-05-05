"""
idea: 
- town: node
- road: edge
- road networks: connected components

=> use bfs, explore and track using a visted set
"""
from collections import deque

def create_graph(towns, roads):
    hashmap={}
    for town in towns:
        hashmap[town]=[]
    
    for road in roads:
        u= road[0]
        v=road[1]

        hashmap[u].append(v)
        hashmap[v].append(u)
    
    return hashmap

def count_road_networks(towns, roads):
    #if have node but no edge
    if len(roads)==0:
        return len(towns)

    #if no node
    if len(towns)==0:
        return 0
    
    #generate graph
    graph= create_graph(towns, roads)

    visited=set()
    network_count=0

    def bfs(node):
        queue=deque()
        queue.append(node)

        while queue:
            removed_node= queue.popleft()

            if removed_node not in visited:
                visited.add(removed_node)

                for neighbor in graph[removed_node]:
                    queue.append(neighbor)


    for town in towns:
        if town not in visited:
            bfs(town)
            network_count+=1
    
    return network_count
