# spent 45 minutes
# bfs 
# TC - O(V+E)
# SC - O(V) for visited set and O(V+E) for adjacency list

from collections import deque


def alternatingPaths(source: str, destination: str, graph: list[tuple[str, str, str]]) -> int:
    # build adjacency list
    adj = {} # source : (destination, color)
    for src, dest, color in graph:
        if src in adj:  
            adj[src].append((dest, color))
        else:
            adj[src] = [(dest, color)]
            
        
    # bfs queue
    queue = deque() # (node, last color, distance)
    queue.append( (source, None, 0) )
    # visited set  
    visited = set() # (node, last color)
    visited.add( (source, None) )
    
    while queue:
        node, last_color, dist = queue.popleft()
        
        if node == destination: # found
            return dist
        
        for nei, color in adj[node]: # check adjacency list
            if color != last_color: # enqueue only if alternating path
                state = (nei, color) 
                if state not in visited: # enqueue only if new path
                    visited.add(state)
                    queue.append( (nei, color, dist+1) )
    
    return -1 # no alternating path


    
    
    
if __name__ == "__main__":
    graph = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]
    src1 = "A"
    dest1 = "E"
    print("Expected: 4")
    print("Actual:", alternating_path(src1, dest1, graph))
    
    src2 = "E"
    dest2 = "D"
    print("Expected: -1")
    print("Actual", alternating_path(src2, dest2, graph))
        
    
