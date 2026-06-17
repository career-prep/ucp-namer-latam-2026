# Data Structure: Graph
# Algorithm: Breadth-first search
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import deque, defaultdict

def alternatingPath(edges, origin, destination):
    if origin == destination:
        return 0
        
    adj = defaultdict(list)
    for u, v, color in edges:
        adj[u].append((v, color))
        
    queue = deque([(origin, 0, None)])
    visited = set()
    
    while queue:
        u, dist, last_color = queue.popleft()
        
        for v, color in adj[u]:
            if color != last_color:
                if v == destination:
                    return dist + 1
                
                if (v, color) not in visited:
                    visited.add((v, color))
                    queue.append((v, dist + 1, color))
                    
    return -1

def main():
    edges1 = [
        ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), 
        ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), 
        ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")
    ]
    print(f"Test Case 1 - Result: {alternatingPath(edges1, 'A', 'E')}")
    print(f"Test Case 2 - Result: {alternatingPath(edges1, 'E', 'D')}")

if __name__ == "__main__":
    main()

# Time Spent: 28 minutes