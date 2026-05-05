# Technique: Dijkstra-like BFS (Shortest Path with Travel/Stopover Penalties)

from collections import deque

def vacationDestinations(edges, origin, k): # Time Complexity: O(V + E), Space Complexity: O(V + E)
    # 1. Build adjacency list where edges store destination and travel time
    adj = {}
    for u, v, time in edges:
        if u not in adj: adj[u] = []
        if v not in adj: adj[v] = []
        # Edges are undirected based on "reached directly from each other"
        adj[u].append((v, time))
        adj[v].append((u, time))

    # 2. Result set to store unique destinations reachable within time k
    reachable = []
    
    # 3. BFS Queue: (current_city, total_time_accumulated)
    # Using a queue because "unweighted" in terms of stopovers, 
    # but we track cumulative time.
    queue = deque([(origin, 0)])
    
    # 4. visited_min_time tracks the best (lowest) time found to reach each city
    # This is crucial because a stopover adds 1 hour, so paths matter.
    visited_min_time = {origin: 0}

    while queue:
        curr_city, curr_time = queue.popleft()

        if curr_city in adj:
            for neighbor, travel_time in adj[curr_city]:
                # 5. Calculate total time: current + travel + 1 hour stopover penalty
                # Note: Stopover penalty is only added if we aren't starting from origin
                stopover_penalty = 1 if curr_city != origin else 0
                new_time = curr_time + travel_time + stopover_penalty

                # 6. If within limit and better than any previously found path
                if new_time <= k:
                    if neighbor not in visited_min_time or new_time < visited_min_time[neighbor]:
                        visited_min_time[neighbor] = new_time
                        queue.append((neighbor, new_time))

    # 7. Collect all cities reached (excluding origin)
    for city in visited_min_time:
        if city != origin:
            reachable.append(city)
            
    # Sort for consistent output comparison
    return sorted(reachable)

class Test:
    def run_tests(self):
        edges = [
            ("Boston", "New York", 4), 
            ("New York", "Philadelphia", 2), 
            ("Boston", "Newport", 1.5), 
            ("Washington, D.C.", "Harper's Ferry", 1), 
            ("Boston", "Portland", 2.5), 
            ("Philadelphia", "Washington, D.C.", 2.5)
        ]
        
        # 1. Test k=5
        # New York is 4 hrs. Philadelphia is 4 + 2 + 1(stopover) = 7 (Fail).
        # Newport is 1.5 (Pass).
        res1 = vacationDestinations(edges, "Boston", 5)
        assert "New York" in res1
        assert "Newport" in res1
        assert len(res1) == 2
        
        # 2. Test k=8
        res2 = vacationDestinations(edges, "New York", 8)
        # To Washington D.C.: Philly(2) + 1(stop) + DC(2.5) = 5.5 (Pass)
        # To Harper's Ferry: DC(5.5) + 1(stop) + HF(1) = 7.5 (Pass)
        assert "Washington, D.C." in res2
        assert "Harper's Ferry" in res2
        assert "Boston" in res2

        print("VacationDestinations tests passed")

if __name__ == "__main__":
    tester = Test()
    tester.run_tests()

# Time complexity: O(V + E) - Standard BFS complexity.
# Space complexity: O(V + E) - Adjacency list and visited tracking.