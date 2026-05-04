#Time: O(E log V)
#Space: O(V + E)

import heapq
from collections import defaultdict
import unittest

def reachable_within_k(edges, origin, k):
    graph = defaultdict(list)

    for u, v, t in edges:
        graph[u].append((v, t))
        graph[v].append((u, t))

    heap = [(0, origin)]
    dist = {origin: 0}

    while heap:
        time, city = heapq.heappop(heap)

        if time > dist.get(city, float('inf')):
            continue

        for nei, travel_time in graph[city]:
            extra = 1 if city != origin else 0
            new_time = time + travel_time + extra

            if new_time < dist.get(nei, float('inf')):
                dist[nei] = new_time
                heapq.heappush(heap, (new_time, nei))

    count = 0
    for city, time in dist.items():
        if city != origin and time <= k:
            count += 1

    return count


#Tests
class TestVacationDestinations(unittest.TestCase):

    def test_basic(self):
        edges = [("A","B",1),("B","C",1)]
        self.assertEqual(reachable_within_k(edges,"A",3), 2)

    def test_zero_reach(self):
        edges = [("A","B",10)]
        self.assertEqual(reachable_within_k(edges,"A",1), 0)

    def test_multiple_paths(self):
        edges = [("A","B",1),("A","C",1),("B","D",1)]
        self.assertEqual(reachable_within_k(edges,"A",3), 3)


if __name__ == "__main__":
    unittest.main()

#Time-taken: 30 minutes