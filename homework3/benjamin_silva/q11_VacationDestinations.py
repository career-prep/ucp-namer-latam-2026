from collections import defaultdict
import heapq

def vacationDestinations(origin, k, edges):
    graph = defaultdict(set)
    for a, b, time in edges:
        graph[a].add((b, time))
        graph[b].add((a, time))
    
    heap = [(0, origin)]
    visited = {}

    while heap:
        time, city = heapq.heappop(heap)

        if city in visited:
            continue
        visited[city] = time

        for neighbor, travel_time in graph[city]:
            if neighbor not in visited:
                arrival = time + travel_time + (1 if city != origin else 0)
                heapq.heappush(heap, (arrival, neighbor))
    
    count = 0
    for city, time in visited.items():
        if city != origin and time <= k:
            count += 1
    return count
        

if __name__ == "__main__":

    edges1 = [
        ("Boston", "New York", 4), ("New York", "Philadelphia", 2),
        ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1),
        ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)
    ]

    print("Test 1 (expect 2):", vacationDestinations("New York", 5, edges1))

    print("Test 2 (expect 4):", vacationDestinations("New York", 7, edges1))

    print("Test 3 (expect 6):", vacationDestinations("New York", 8, edges1))