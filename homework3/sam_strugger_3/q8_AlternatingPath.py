# Data structure is a graph. This is a shortest path problem so I'd use BFS.
# Not sure on complexity, didn't finish this one.

def alternatingPath(towns, destination):
    # Plan
    # Make adjaceny set graph 
    # This is shortest path problem so use bfs 
    # We need to keep track of what edge color 
    # we came from 
    # In our queue we can append the node and the
    # color to keep track
    
    red_adj = {}
    blue_adj = {}
    for town in towns:
        red_adj[town] = []
        blue_adj[town] = []

    for t1, t2, color in edges:
        if color == "red":
            red_adj[t1].append(t2)
        else:
            blue_adj[t1].append(t2)


    queue = deque()
    queue.append([A,None]) # this will be the node and color
    
    visit = set()
    visit.add()
    
    # I am really lost on this problem


