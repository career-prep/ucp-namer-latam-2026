# Data Structure: Graph
# Algorithm: Djikstra's Algorithm
# Time Complexity: O(E log V) where E is the # of roads and V is the # of cities
# Space Complexity: O(V + E) to store the graph and seen states

import heapq
from collections import defaultdict

def vacation_destinations(origin, k, pairs):
    graph = defaultdict(list)
    for u, v, weight in pairs:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    pq = [(0, origin)]

    while pq:
        curr_time, u = heapq.heappop(pq)

        for v, weight in graph[u]:
            stopover = 1 if u != origin else 0
            new_time = curr_time + weight + stopover


# Time Spent: 40 min (ran out of time). Was able to determine the algorithm for the question
# but barely studied up on how to implement Djikstra. 