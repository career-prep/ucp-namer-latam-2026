# Data Structure: Graph
# Algorithm: Depth-First Search (DFS)
# Time Complexity: O(V!)
# Space Complexity: O(V)

from collections import defaultdict

def vacationDestinations(origin, k, travel_times):
    adj = defaultdict(list)
    for u, v, time in travel_times:
        adj[u].append((v, time))
        adj[v].append((u, time))
    
    reachable_cities = set()
    
    def discover(current_city, current_time, visited):
        if current_time > k:
            return
            
        if current_city != origin:
            reachable_cities.add(current_city)
            
        for neighbor, travel_time in adj[current_city]:
            if neighbor not in visited:
                stopover = 1 if current_city != origin else 0
                new_time = current_time + travel_time + stopover
                
                if new_time <= k:
                    visited.add(neighbor)
                    discover(neighbor, new_time, visited)
                    visited.remove(neighbor)

    discover(origin, 0, {origin})
    
    results = sorted(list(reachable_cities))
    return len(results), results

def main():
    travel_data = [
        ("Boston", "New York", 4),
        ("New York", "Philadelphia", 2),
        ("Boston", "Newport", 1.5),
        ("Washington, D.C.", "Harper's Ferry", 1),
        ("Boston", "Portland", 2.5),
        ("Philadelphia", "Washington, D.C.", 2.5)
    ]

    count1, cities1 = vacationDestinations("New York", 5, travel_data)
    print(f"Test Case 1 (k=5) - Count: {count1}, Cities: {cities1}")

    count2, cities2 = vacationDestinations("New York", 7, travel_data)
    print(f"Test Case 2 (k=7) - Count: {count2}, Cities: {cities2}")

    count3, cities3 = vacationDestinations("New York", 8, travel_data)
    print(f"Test Case 3 (k=8) - Count: {count3}, Cities: {cities3}")

if __name__ == "__main__":
    main()

# Time Spent: 35 minutes