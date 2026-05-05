# Method: BFS
# Space Complexity: O(V + E)
# Time Complexity: O(V + E)
# Total Time Taken: 40 mins

from collections import deque

def AlternatingPath(origin, destination, list):
    graph = {}

    for V, E, color in list:
        if V not in graph: graph[V] = set()
        graph[V].add((E, color))

    queue = deque([
    (origin, 0, "red"), 
    (origin, 0, "blue")  
    ])  

    seen = {(origin, "red"), (origin, "blue")}

    while queue:
        cur, dist, last_color = queue.popleft()
        if cur == destination:
            return dist
    
        for neighbor, color in graph.get(cur, []):
            if (neighbor, color) not in seen and color != last_color:
                    queue.append((neighbor, dist + 1, color))
                    seen.add((neighbor, color))
    return -1



edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), 
         ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]

print(AlternatingPath("A", "E", edges)) # Expected Output: 4
print(AlternatingPath("E", "D", edges)) # Expected Output: -1