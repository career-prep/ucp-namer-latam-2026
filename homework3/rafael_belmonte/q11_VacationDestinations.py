# Data Structure: Graph (weighted, undirected) backed by an adjacency list
# Algorithm: Dijkstra's shortest paths (Priority Queue / Min-Heap as the frontier)
#
# Each city is a node; each route pair is an undirected weighted edge.
# A stopover (any intermediate city) costs +1 hour, so when relaxing an edge
# u -> v we add edge_weight, plus +1 if u is not the origin (i.e., u itself is
# being used as a stopover). Then any city whose shortest reach <= k counts.
#
# NOTE: The PDF's example "Output" numerics appear inconsistent with the cities
# they list; this implementation follows the textual descriptions (which list
# the destinations explicitly).
#
# Time complexity:  O((V + E) log V)
# Space complexity: O(V + E)

import heapq
from collections import defaultdict


def vacation_destinations(routes, origin, k):
    graph = defaultdict(list)
    for a, b, t in routes:
        graph[a].append((b, t))
        graph[b].append((a, t))

    # Dijkstra with stopover surcharge
    best = {origin: 0.0}
    heap = [(0.0, origin)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > best[node]:
            continue
        for nbr, edge_t in graph[node]:
            stopover = 0 if node == origin else 1
            new_dist = dist + edge_t + stopover
            if new_dist < best.get(nbr, float("inf")):
                best[nbr] = new_dist
                heapq.heappush(heap, (new_dist, nbr))

    # exclude origin itself from the destination count
    reachable = [city for city, d in best.items() if city != origin and d <= k]
    return len(reachable), sorted(reachable)


# test cases
if __name__ == "__main__":
    routes = [
        ("Boston", "New York", 4),
        ("New York", "Philadelphia", 2),
        ("Boston", "Newport", 1.5),
        ("Washington, D.C.", "Harper's Ferry", 1),
        ("Boston", "Portland", 2.5),
        ("Philadelphia", "Washington, D.C.", 2.5),
    ]

    n5, r5 = vacation_destinations(routes, "New York", 5)
    print("k=5:", n5, r5)
    assert n5 == 2 and set(r5) == {"Boston", "Philadelphia"}

    n7, r7 = vacation_destinations(routes, "New York", 7)
    print("k=7:", n7, r7)
    # NY->Philadelphia(2), NY->Boston(4), NY->Philadelphia->DC(5.5),
    # NY->Boston->Newport(6.5)
    assert n7 == 4 and set(r7) == {
        "Boston", "Philadelphia", "Washington, D.C.", "Newport"
    }

    n8, r8 = vacation_destinations(routes, "New York", 8)
    print("k=8:", n8, r8)
    # adds Portland (4+1+2.5=7.5) and Harper's Ferry (2+1+2.5+1+1=7.5)
    assert n8 == 6 and set(r8) == {
        "Boston", "Philadelphia", "Washington, D.C.", "Newport",
        "Portland", "Harper's Ferry"
    }

    print("yay!!")

# Time spent: ~30 minutes
