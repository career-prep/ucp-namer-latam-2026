# Algorithm: Dijkstra's shortest path with a stopover penalty
# Edges are bidirectional. Each non-origin city we depart from adds a 1-hour stopover.
# Time Complexity: O((V + E) log V)
# Space Complexity: O(V + E)

import heapq


def vacationDestinations(edges, origin, k):
    graph = {}
    for a, b, t in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, t))
        graph[b].append((a, t))

    if origin not in graph:
        return 0

    dist = {origin: 0}
    heap = [(0, origin)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue
        for v, t in graph[u]:
            stopover = 0 if u == origin else 1
            new_d = d + stopover + t
            if new_d < dist.get(v, float("inf")):
                dist[v] = new_d
                heapq.heappush(heap, (new_d, v))

    count = 0
    for node, d in dist.items():
        if node != origin and d <= k:
            count += 1
    return count


print("VacationDestinations Results:")

edges = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5),
]

print(vacationDestinations(edges, "New York", 5))
print(vacationDestinations(edges, "New York", 7))
print(vacationDestinations(edges, "New York", 8))
print(vacationDestinations(edges, "Boston", 5))
print(vacationDestinations(edges, "Reykjavik", 100))
