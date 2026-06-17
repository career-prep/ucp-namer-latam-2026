from collections import defaultdict

# Data Structure: Graph (Adjacency List)
# Algorithm: DFS with Branch Pruning
# Time Complexity: O(cities + roads)
# Space Complexity: O(cities + roads)


def vacation_destinations(roads, origin, k):
    # Build weighted undirected graph
    graph = defaultdict(list)

    for city1, city2, travel_time in roads:
        graph[city1].append((city2, travel_time))
        graph[city2].append((city1, travel_time))

    # Store reachable destinations
    reachable = set()

    # DFS function
    def dfs(current_city, total_time, visited):
        # If total time exceeds k, stop exploring
        if total_time > k:
            return

        # Add reachable city (but not the origin itself)
        if current_city != origin:
            reachable.add(current_city)

        # Explore neighbors
        for neighbor, travel_time in graph[current_city]:

            # Avoid cycles
            if neighbor not in visited:

                # Add stopover penalty if leaving an intermediate city
                stopover = 0
                if current_city != origin:
                    stopover = 1

                new_time = total_time + travel_time + stopover

                visited.add(neighbor)
                dfs(neighbor, new_time, visited)
                visited.remove(neighbor)

    # Start DFS
    dfs(origin, 0, {origin})

    return len(reachable)


def run_tests():

    roads = [
        ("Boston", "New York", 4),
        ("New York", "Philadelphia", 2),
        ("Boston", "Newport", 1.5),
        ("Washington, D.C.", "Harper's Ferry", 1),
        ("Boston", "Portland", 2.5),
        ("Philadelphia", "Washington, D.C.", 2.5)
    ]

    # Example 1
    assert vacation_destinations(roads, "New York", 5) == 2

    # Example 2
    assert vacation_destinations(roads, "New York", 7) == 4

    # Example 3
    assert vacation_destinations(roads, "New York", 8) == 6

    # Edge cases
    assert vacation_destinations([], "Boston", 5) == 0
    assert vacation_destinations(roads, "Chicago", 5) == 0
    assert vacation_destinations(roads, "New York", 0) == 0

    print("All tests passed")


if __name__ == "__main__":
    run_tests()