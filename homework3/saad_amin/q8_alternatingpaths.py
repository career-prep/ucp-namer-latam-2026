#Time Complexity: O(N + E)
#Space Complexity: O(N + E)
#Technique: Graphs(BFS)

from collections import deque, defaultdict

def alternatingPath(edges, origin, destination):
    graph = defaultdict(list)
    
    for u, v, color in edges:
        graph[u].append((v, color))
    
    queue = deque()
    queue.append((origin, None, 0))
    
    visited = set()
    
    while queue:
        node, last_color, dist = queue.popleft()
        
        if node == destination:
            return dist
        
        for nei, color in graph[node]:
            if color != last_color and (nei, color) not in visited:
                visited.add((nei, color))
                queue.append((nei, color, dist + 1))
    
    return -1

edges = [
    ("A","B","blue"), ("A","C","red"),
    ("B","D","blue"), ("B","E","blue"),
    ("C","B","red"), ("D","C","blue"),
    ("A","D","red"), ("D","E","red"),
    ("E","C","red")
]

print(alternatingPath(edges, "A", "E"))  #4
print(alternatingPath(edges, "E", "D"))  #-1

#Tine: 32 min