# Data Structure: Graph
# Algorithm: BFS (Dijkstra's for weighted shortest path)
# Time Complexity: O((V + E) log V)
# Space Complexity: O(V + E)

# we assume stopover adds an hour.

import heapq
from collections import defaultdict

def vacationDestinations(connections, origin, k):
    graph = defaultdict(list)
    for a, b, time in connections:
        graph[a].append((b, time))
        graph[b].append((a, time))

    dist = {origin: 0}
    heap = [(0, origin)]

    while heap:
        cost, city = heapq.heappop(heap)
        if cost > dist.get(city, float('inf')):
            continue
        for neighbor, travel_time in graph[city]:
            stopover = 1 if city != origin else 0
            new_cost = cost + travel_time + stopover
            if new_cost < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return sum(1 for city, t in dist.items() if city != origin and t <= k)

connections = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

print(vacationDestinations(connections, "New York", 5)) 
print(vacationDestinations(connections, "New York", 7)) 
print(vacationDestinations(connections, "New York", 8))

# Time spent: 120 minutes
