# Data Structure: Graph, Priority Queue
# Algorithm: Generic traversal
# Time Complexity: _
# Space Complexity: O(V + E)

import heapq

def vacation_destinations(edges, origin, k):
    graph = {}
    for u, v, t in edges:
        # build undirected weighted graph
        graph.setdefault(u, []).append((v, t))
        graph.setdefault(v, []).append((u, t))

    heap = [(0, origin, 0)]
    best = {origin: 0}

    # store reachable destinations
    result = set()

    while heap:
        # always process node with smallest time first
        time, node, edges_used = heapq.heappop(heap)

        for nei, t in graph.get(node, []):
            # number of edges increases
            new_edges = edges_used + 1
            new_time = time + t + (0 if edges_used == 0 else 1)

            # update if better path found within k
            if new_time <= k and (nei not in best or new_time < best[nei]):
                best[nei] = new_time
                heapq.heappush(heap, (new_time, nei, new_edges))

                # add valid destination
                if nei != origin:
                    result.add(nei)

    return len(result) # number of reachable destinations

# Time Taken: 34mins 53secs

# Test Case
edges = [("Boston","New York",4),("New York","Philadelphia",2),("Boston","Newport",1.5),
         ("Washington D.C.","Harper's Ferry",1),("Boston","Portland",2.5),
         ("Philadelphia","Washington D.C.",2.5)]

print(vacation_destinations(edges, "New York", 5))
print(vacation_destinations(edges, "New York", 7))
print(vacation_destinations(edges, "New York", 8))

# Edge Cases
print(vacation_destinations([], "A", 5))
print(vacation_destinations([("A","B",10)], "A", 5))
print(vacation_destinations([("A","B",1)], "A", 2))