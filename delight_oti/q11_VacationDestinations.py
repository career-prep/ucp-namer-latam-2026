from collections import deque

def VacationDestinations(routes, origin, k):
    graph = {}

    for city1, city2, time in routes:
        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []

        graph[city1].append((city2, time))
        graph[city2].append((city1, time))

    queue = deque()
    queue.append((origin, 0))

    best_time = {}
    best_time[origin] = 0

    reachable = set()

    while queue:
        city, current_time = queue.popleft()

        for neighbor, travel_time in graph[city]:
            extra_stopover = 0

            if city != origin:
                extra_stopover = 1

            new_time = current_time + extra_stopover + travel_time

            if new_time <= k:
                if neighbor != origin:
                    reachable.add(neighbor)

                    if neighbor not in best_time or new_time < best_time[neighbor]:
                        best_time[neighbor] = new_time
                        queue.append((neighbor, new_time))

    return len(reachable)

routes = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

# origin = "New York"
# k = 5

# origin = "New York"
# k = 7

# origin = "New York"
# k = 8

# print(VacationDestinations(routes, origin, k))

# 40