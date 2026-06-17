#Time: 40 minutes
# BFS
graph = {}
def AlternatingPath(origin, destination, edges):
    for src, dst, color in edges:
        if src not in graph:
            graph[src] = []
        if dst not in graph:
            graph[dst] = []

    for src, dst, color in edges:
        graph[src].append((dst,color))

    q = [(origin, "red", 0), (origin, "blue", 0)]
    visited = set()

    while q:
        node, last_color, length = q.pop(0)
        
        if node == destination:
            return length
        
        if (node, last_color) in visited:
            continue
        
        visited.add((node, last_color))
        next_color = "blue" if last_color == "red" else "red"
        
        for neighbor, edge_color in graph[node]:
            if edge_color == next_color:
                q.append((neighbor, next_color, length + 1))
    return -1

edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]

#Input: origin = A, destination = E
#Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))

#Input: origin = E, destination = D
#Output: -1 (only path is: E→C (red), C→B (red), B→D (blue))

print(AlternatingPath("A", "E", edges))  
print(AlternatingPath("E", "D", edges))  