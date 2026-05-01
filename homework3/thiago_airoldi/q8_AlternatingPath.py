# Graph Traversal - BFS
# O(V + E) Time Complexity because of BFS. V is the number of nodes (vertices), E is the number of edges.
# O(V + E) Space Complexity because of the adjacency list.
# Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of the shortest path from the origin to the destination 
# in which the edges traversed alternate in color. Return -1 if no such path exists.

from collections import defaultdict # To avoid key error
from collections import deque

def AlternatingPath(paths, origin, destination):

    if not paths:
        return -1
    
    # 1. Create Adjacency List
    graph = defaultdict(list)

    for start, end, color in paths:
        graph[start].append((end, color)) 


    
    # I would clarify this in an interview, but I am assuming that before traversing we do not have a predefined color, which means we can choose a valid path
    # that is either red or blue to start. After that start, we then have to follow the alternating path rule.

    visited = set()

    # 2. Initialize queue with all of the origin's neighbors
    q = deque()

    for nei, color in graph[origin]:
        q.append((nei, color, 1)) # The '1' is the distance from the origin.
        visited.add((nei, color))



    # 3. BFS until we reach destination or exhaust all paths
    while q:

        cur, lastColor, dist = q.popleft()

        if cur == destination:
            return dist
        
        for nei, nextColor in graph[cur]:
            # Only add nodes that we have not visited, and is a color that's different than our current color
            if nextColor != lastColor and (nei, nextColor) not in visited:
                visited.add((nei, nextColor))
                q.append((nei, nextColor, dist+1))
        


    # A valid path was not found
    return -1



# 29 minutes

# Test Cases

paths1 = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), 
          ("E", "C", "red")]

paths2 = []

origin1 = "A"
destination1 = "E"

origin2 = "E"
destination2 = "D"


print(AlternatingPath(paths1, origin1, destination1))
print(AlternatingPath(paths1, origin2, destination2))

# My Added Test Cases
print(AlternatingPath(paths2, origin1, destination1))






