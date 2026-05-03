#Time Complexity: O(E log V)
#Space : O(V + E)
#Technique: Heaps and BFS(Dijktsra)

import heapq
from collections import defaultdict

def vacationDestinations(edges, origin, k):
    graph = defaultdict(list)

    for city1, city2, time in edges:
        graph[city1].append((city2, time))
        graph[city2].append((city1, time))

    heap = [(0, origin)]
    shortest = {origin: 0}

    while heap:
        curr_time, city = heapq.heappop(heap)

        if curr_time > shortest[city]:
            continue

        for nei, travel_time in graph[city]:
            extra_stop_time = 0 if city == origin else 1
            new_time = curr_time + travel_time + extra_stop_time

            if new_time < shortest.get(nei, float("inf")):
                shortest[nei] = new_time
                heapq.heappush(heap, (new_time, nei))

    count = 0
    for city in shortest:
        if city != origin and shortest[city] <= k:
            count += 1

    return count

edges = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

print(vacationDestinations(edges, "New York", 5))  # 2
print(vacationDestinations(edges, "New York", 7))  # 4
print(vacationDestinations(edges, "New York", 8))  # 6

#time: 40 min
