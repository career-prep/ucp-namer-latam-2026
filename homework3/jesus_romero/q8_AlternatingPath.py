# Technique: BFS on a State-Space Graph (Shortest Path with Edge Attributes)

from collections import deque

def shortestAlternatingPath(edges, origin, destination): # Time, Space Complexities: O(V + E), O(V + E)
    # 1. Build adjacency list where edges store destination and color
    # Format: adj[node] = [(neighbor, color), ...]
    adj = {}
    for u, v, color in edges:
        if u not in adj: adj[u] = []
        adj[u].append((v, color))
        if v not in adj: adj[v] = [] # Ensure destination exists in map

    # 2. BFS Queue stores: (current_node, length, last_color_traversed)
    # last_color can be None for the starting node
    queue = deque([(origin, 0, None)])
    
    # 3. Visited set tracks (node, color_used_to_reach_it) 
    # to allow visiting the same node via different colored edges
    visited = set()

    while queue:
        curr, dist, last_color = queue.popleft()

        if curr == destination:
            return dist

        if curr in adj:
            for neighbor, color in adj[curr]:
                # 4. Only proceed if the edge color alternates and state is unvisited
                if color != last_color and (neighbor, color) not in visited:
                    visited.add((neighbor, color))
                    queue.append((neighbor, dist + 1, color))

    return -1

class Test:
    def run_tests(self):
        # 1. Test Case: Alternating path exists
        edges1 = [
            ('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), 
            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), 
            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")
        ]
        # Path: A -> D (red) -> C (blue) -> B (red) -> E (blue)
        assert shortestAlternatingPath(edges1, 'A', 'E') == 4
        
        # 2. Test Case: No alternating path possible
        edges2 = [('E', 'C', "red"), ('C', 'B', "red"), ('B', 'D', "blue")]
        assert shortestAlternatingPath(edges2, 'E', 'D') == -1
        
        # 3. Test Case: Destination is origin
        assert shortestAlternatingPath([], 'A', 'A') == 0

        print("ShortestAlternatingPath tests passed")

if __name__ == "__main__":
    tester = Test()
    tester.run_tests()

# Time complexity: O(V + E) - BFS visits each edge/state once.
# Space complexity: O(V + E) - for the adjacency list and queue.
