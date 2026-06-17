# Data structure: Graph + Min-Heap (Dijkstra)
# Time: O((V + E) log V)
# Space: O(V + E)

import heapq


def count_vacation_destinations(routes, origin, k):
    graph = {}
    for a, b, travel_time in routes:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, travel_time))
        graph[b].append((a, travel_time))

    if origin not in graph:
        return 0

    dist = {origin: 0}
    heap = [(0, origin)]

    while heap:
        cur_time, city = heapq.heappop(heap)
        if cur_time > dist.get(city, float("inf")):
            continue

        for nxt, edge_time in graph[city]:
            stopover_penalty = 0 if city == origin else 1
            new_time = cur_time + edge_time + stopover_penalty
            if new_time < dist.get(nxt, float("inf")):
                dist[nxt] = new_time
                heapq.heappush(heap, (new_time, nxt))

    reachable = [city for city, t in dist.items() if city != origin and t <= k]
    return len(reachable)


routes = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

print("Correct:", 2)
print("Output: ", count_vacation_destinations(routes, "New York", 5))
print()

print("Correct:", 4)
print("Output: ", count_vacation_destinations(routes, "New York", 7))
print()

print("Correct:", 6)
print("Output: ", count_vacation_destinations(routes, "New York", 8))
print()

# time taken: 35 min
