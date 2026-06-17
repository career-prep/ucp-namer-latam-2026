# Time complexity: O((V + E) log V) I think?
# Space complexity: O(V + E), V = # of cities, E = # of paths between cities

# Technique: Dijkstra's algorithm (this wasn't in the listed techniques section, was I supposed to use something else?)
import heapq

def VacationDestinations(edges, origin, k):
    graph = {}

    for u, v, t in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, t))
        graph[v].append((u, t))

    heap = [(0, origin)]  
    dist = {origin: 0}

    while heap:
        time, node = heapq.heappop(heap)

        if time > dist.get(node, float('inf')):
            continue

        for neighbor, travel_time in graph.get(node, []):
            extra = 0 if node == origin else 1
            new_time = time + travel_time + extra

            if new_time < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))

    return sum(1 for node, t in dist.items() if node != origin and t <= k)

if __name__ == "__main__":
    edges = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

    inputs = [
        ("New York", 5),
        ("New York", 7),
        ("New York", 8)
    ]

    for origin, k in inputs:
        print(f"Output: {VacationDestinations(edges, origin, k)}")

# ~ time spent: 45 minutes
