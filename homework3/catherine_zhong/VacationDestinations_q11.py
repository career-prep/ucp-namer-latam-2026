#time complexity: O((n+m)logn)
#data structure: heap

import heapq
from collections import defaultdict

def VacationDestinations(routes, start, k):
    graph = defaultdict(list)

    for a, b, t in routes:
        graph[a].append((b,t))
        graph[b].append((a,t))

    heap = [(0, start, 0)]
    bestTime = {start: 0}

    while heap:
        time, origin, stops = heapq.heappop(heap)

        for dest, t in graph[origin]:
            extra = 1 if stops >= 1 else 0
            newTime = time + t + extra

            if dest not in bestTime or newTime < bestTime[dest]:
                bestTime[dest] = newTime
                heapq.heappush(heap, (newTime, dest, stops+1))


    result = [city for city, t in bestTime.items() if city != start and t <= k]
    return len(result)

#test cases:
paths= [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

Origin = "New York"
k=5 
print(f'test 1: {VacationDestinations(paths, Origin, k)}')

k=7 
print(f'test 2: {VacationDestinations(paths, Origin, k)}')

k=8
print(f'test 3: {VacationDestinations(paths, Origin, k)}')
#time spent: 35 min

