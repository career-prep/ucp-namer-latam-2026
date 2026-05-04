# Data Structure: Graph + BFS
# Technique: BFS tracking cumulative travel time (edge weight + 1hr stopover per city)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import deque

def vacationDestinations(edges, origin, k):
    # build undirected weighted adjacency list
    graph = {}
    for u, v, time in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, time))
        graph[v].append((u, time))

    visited = {origin: 0}   # city -> best time we arrived at it
    queue   = deque([(origin, 0)])
    count   = 0

    while queue:
        city, timeSoFar = queue.popleft()

        for neighbor, travelTime in graph.get(city, []):
            arrivalTime = timeSoFar + travelTime + (1 if city != origin else 0)

            if arrivalTime <= k and (neighbor not in visited or visited[neighbor] > arrivalTime):
                visited[neighbor] = arrivalTime
                queue.append((neighbor, arrivalTime))

    count = sum(1 for city in visited if city != origin)
    return count


edges = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

# Test 1: origin="New York", k=5 -> 2 (Boston, Philadelphia.)
print(vacationDestinations(edges, "New York", 5))   # 2

# Test 2: origin="New York", k=7 -> 4 (Boston, Philadelphia., Washington D.C., Newport)
print(vacationDestinations(edges, "New York", 7))   # 4

# Test 3: origin="New York", k=8 -> 6 (all reachable)
print(vacationDestinations(edges, "New York", 8))   # 6

# Test 4: k=0 -> no destinations reachable
print(vacationDestinations(edges, "New York", 0))   # 0

# Test 5: k=4 -> only direct neighbor Boston (4hrs, no stopover from origin)
print(vacationDestinations(edges, "New York", 4))   # 1 (Boston only, Philadelphia. needs 2+1=3 but Newport unreachable)

# Time spent: ~40 minutes