import heapq

# Data Structure: Graph, Hashmap,  Heap
# Algorithm: Graph + Priority Queue
# Time Complexity: O((V + E) log V)
# Space Complexity: O(V + E)
# Given an origin city, a max travel time k, and pairs of destinations with travel times, return the number
# of destinations reachable within k hours (each stopover at an intermediate city adds 1 hour).


def vacationDestinations(origin, k, connections):
    graph = {}
    for a, b, t in connections:
        graph.setdefault(a, []).append((b, t))
        graph.setdefault(b, []).append((a, t))

    dist = {origin: 0}
    heap = [(0, origin)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist.get(node, float("inf")):
            continue
        stopover = 1 if node != origin else 0
        for neighbor, travel_time in graph.get(node, []):
            new_cost = cost + stopover + travel_time
            if new_cost < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    reachable = [city for city, d in dist.items() if city != origin and d <= k]
    return len(reachable), sorted(reachable)


# Testing:
connections = [
    ("New York", "Philadelphia", 2),
    ("New York", "Boston", 4),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harpers Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

n, cities = vacationDestinations("New York", 5, connections)
print(f"k=5: {n} -> {cities}")   # 2: Boston, Philadelphia

n, cities = vacationDestinations("New York", 7, connections)
# 4: Boston, Newport, Philadelphia, Washington D.C.
print(f"k=7: {n} -> {cities}")

n, cities = vacationDestinations("New York", 8, connections)
print(f"k=8: {n} -> {cities}")   # 6: all destinations
