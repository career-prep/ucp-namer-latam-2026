"""
idea: compute a graph, where: key= start_node, val= (end_node, color)
run bfs to find shortest path, check the conditions


"""
from collections import deque

class State:
    def __init__(self, node=None, last_color=None, distance=None):
        self.node=node
        self.last_color=last_color
        self.distance= distance

#key = node, val= (end, color)
def create_graph(edges):
    graph={}
    for edge in edges:

        start= edge[0]
        end= edge[1]
        color= edge[2]

        if start not in graph:
            graph[start]=[]
        graph[start].append((end, color))
    
    return graph


def alternating_path(start, end, edges):
    if len(edges)==0 and start!=end:
        return -1

    if start == end:
        return 0
    
    graph= create_graph(edges)

    queue=deque()
    start_state= State(start, None, 0)
    queue.append(start_state)

    #visted store (node, last_color)
    visited=set()
    visited.add((start, None))

    while queue:
        removed_state= queue.popleft()

        if removed_state.node == end:
            return removed_state.distance
        
        for neighbor, color in graph[removed_state.node]:
            if color!= removed_state.last_color:
                new = (neighbor, color)
                if new not in visited:
                    visited.add(new)
                    queue.append(State(neighbor, color, removed_state.distance+1))
    
    return -1









