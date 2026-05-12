# Technique: BFS on a State-Space Graph (Shortest Path with Edge Attributes)
# Standard shortest-path-on-unweighted-graph problem with an extra constraint:
# consecutive edges must alternate in color. We expand each node into two
# states (node, "blue_last") and (node, "red_last"), plus an initial state
# (origin, None) that may step over either color first. BFS guarantees the
# first time we reach the destination is via a shortest path.
#
# Time complexity:  O((V + E) * 2) = O(V + E)
# Space complexity: O(V * 2)


from collections import deque

def shortestAlternatingPath(edges, origin, destination): # Time, Space Complexities: O(V + E), O(V + E)
    # Build adjacency list where edges store destination and color
    # Format: adj[node] = [(neighbor, color), ...]
    adj = {}
    for u, v, color in edges:
        if u not in adj: adj[u] = []
        adj[u].append((v, color))
        if v not in adj: adj[v] = [] # Ensure destination exists in map

    # BFS Queue stores: (current_node, length, last_color_traversed)
    # last_color can be None for the starting node
    queue = deque([(origin, 0, None)])
    
    # Visited set tracks (node, color_used_to_reach_it) 
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
        # Test Case: Alternating path exists
        edges1 = [
            ('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), 
            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), 
            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")
        ]
        # Path: A -> D (red) -> C (blue) -> B (red) -> E (blue)
        assert shortestAlternatingPath(edges1, 'A', 'E') == 4
        
        #Test Case: No alternating path possible
        edges2 = [('E', 'C', "red"), ('C', 'B', "red"), ('B', 'D', "blue")]
        assert shortestAlternatingPath(edges2, 'E', 'D') == -1
        
        #Test Case: Destination is origin
        assert shortestAlternatingPath([], 'A', 'A') == 0

        print("ShortestAlternatingPath tests passed")
if __name__ == "__main__":
    tester = Test()
    tester.run_tests()
