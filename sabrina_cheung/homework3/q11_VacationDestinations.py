# Method: BFS
# Space Complexity: O(V + E)
# Time Complexity: O(V + E)
# Total Time Taken: 40 mins

from collections import deque

def VacationDestinations(origin, k, destinations):
    graph = {}

    for city1, city2, time in destinations:
        if city1 not in graph: graph[city1] = []
        if city2 not in graph: graph[city2] = []
        graph[city1].append((city2, time))
        graph[city2].append((city1, time))

    queue = deque([(origin, 0)])
    visited = {origin: 0}
    result = set()

    while queue:
        cur, time = queue.popleft()

        for neighbor, travel in graph.get(cur, []):
            stopover = 0 if cur == origin else 1
            totalTime = time + stopover + travel

            if totalTime <= k:
                if neighbor not in visited or totalTime < visited[neighbor]:
                    visited[neighbor] = totalTime
                    result.add(neighbor)
                    queue.append((neighbor, totalTime))

    return len(list(result))

destinations = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
print(VacationDestinations("New York", 5, destinations)) # Expected: 2
print(VacationDestinations("New York", 7, destinations)) # Expected: 4
print(VacationDestinations("New York", 8, destinations)) # Expected: 6