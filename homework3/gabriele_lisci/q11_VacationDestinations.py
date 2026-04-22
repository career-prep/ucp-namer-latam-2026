# Runtime: O(V + E)
# Space complexity: O(V + E)
# Data Structure: Graph
# Algorithm: BFS

import collections
def vacationDestinations(pairs, origin, k):
    graph = collections.defaultdict(list)
    for a, b, weight in pairs:
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    q = collections.deque()
    time = 0
    q.append((origin, time))
    visited = set()
    visited.add(origin)
    res = 0
    while q:
        curr, time = q.popleft()
        for nei, flytime in graph[curr]:
            currTime = time + flytime
            if nei not in visited and currTime <= k:
                res += 1
                visited.add(nei)
            if currTime + 1 <= k:
                q.append((nei, currTime+1))
    return res



pairs1 = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
# Generic Test Cases:
print(vacationDestinations(pairs1, "New York", 5) == 2)
print(vacationDestinations(pairs1, "New York", 7) == 4)
print(vacationDestinations(pairs1, "New York", 8) == 6)
# City not in graph
print(vacationDestinations(pairs1, "DNE", 8) == 0)
# 0 distance
print(vacationDestinations(pairs1, "New York", 0) == 0)

pairs2 = [("A", "B", 1), ("B", "C", 2)]
# Layover Test
print(vacationDestinations(pairs2, "A", 3) == 1)

# Time Spent: 35:00
