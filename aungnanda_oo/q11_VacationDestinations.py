# Question 11: VacationDestinations

# Data Structure: Graph (weighted, undirected)
# Algorithm: Dijkstra's algorithm
#   — stopover at each intermediate city adds 1 hour; find all cities
#     reachable from origin within k total hours
# Time Complexity: O((V + E) log V)
# Space Complexity: O(V + E)

import heapq


def vacationDestinations(connections, origin, k):
    graph = {}
    for a, b, time in connections:
        graph.setdefault(a, []).append((b, time))
        graph.setdefault(b, []).append((a, time))

    dist = {origin: 0}
    heap = [(0, origin)]

    while heap:
        time, city = heapq.heappop(heap)
        if time > dist.get(city, float("inf")):
            continue
        # Leaving an intermediate city costs +1 hr stopover; origin has no stopover
        stopover = 1 if city != origin else 0
        for neighbor, travel_time in graph.get(city, []):
            new_time = time + stopover + travel_time
            if new_time < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))

    return sum(1 for city, t in dist.items() if city != origin and t <= k)


# --- Tests ---

connections = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5),
]

print("NY k=5:", vacationDestinations(connections, "New York", 5))
# 2 (Boston=4, Philadelphia=2)

print("NY k=7:", vacationDestinations(connections, "New York", 7))
# 4 (Boston=4, Philadelphia=2, Newport=6.5, Washington D.C.=5.5)

print("NY k=8:", vacationDestinations(connections, "New York", 8))
# 6 (+ Portland=7.5, Harper's Ferry=7.5)

# Edge cases
print("k=0:", vacationDestinations(connections, "New York", 0))    # 0
print("k=2:", vacationDestinations(connections, "New York", 2))    # 1 (Philadelphia only)
print("no graph:", vacationDestinations([], "X", 10))              # 0

# Spent a total of 35 mins on this question
