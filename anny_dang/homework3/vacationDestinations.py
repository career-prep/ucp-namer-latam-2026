from collections import defaultdict
import heapq
def vacationDestinations(origin, k, pairs):
    """
    idea:
    Build an undirected weighted graph from the city pairs.
    Use a min-heap to always process the city with the smallest current travel time
    Keep a distance map storing the shortest known time to each city
    For each neighbor, compute the new travel time, including the extra 1 hour
    for a stopover when leaving an intermediate city. If the new time is smaller
    than the previously known time, update it and push it into the heap.
    At the end, count how many cities other than the origin have shortest travel
    time less than or equal to k.

    Time complexity: O((V + E) log V)
    Space complexity: O(V + E)
    """

    graph = defaultdict(list)
    for u, v, weight in pairs:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    
    heap = [(0, origin)]
    dist = {origin: 0}
    while heap:
        cur, city = heapq.heappop(heap)

        if cur != dist[city]:
            continue

        for nei, weight in graph[city]:
            next_time = cur + weight + (0 if city == origin else 1)
            if next_time < dist.get(nei, float("inf")):
                dist[nei] = next_time
                heapq.heappush(heap, (next_time, nei))
                
    return sum(1 for city, time in dist.items() if city != origin and time <= k)


if __name__ == "__main__":
    example_pairs = [
        ("Boston", "New York", 4),
        ("New York", "Philadelphia", 2),
        ("Boston", "Newport", 1.5),
        ("Washington, D.C.", "Harper's Ferry", 1),
        ("Boston", "Portland", 2.5),
        ("Philadelphia", "Washington, D.C.", 2.5),
    ]

    print(vacationDestinations("New York", 5, example_pairs))  # Expected: 2
    print(vacationDestinations("New York", 7, example_pairs))  # Expected: 4
    print(vacationDestinations("New York", 8, example_pairs))  # Expected: 6

