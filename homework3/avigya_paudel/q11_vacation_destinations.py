# Time taken: 37 minutes
# Time complexity: O((V+E)log(V))
# Space complexity: O(V+E), where V = number of cities, and E = number of routes
# Algorithm: Dijkstra's Algorithm + Heap

from collections import defaultdict
import heapq


def vacation_destinations(routes, origin, k):
    """
    Given travel routes, an origin, and a max travel time k, return the number
    of destinations reachable within k hours.
    """
    adj_list = defaultdict(list)
    for city_1, city_2, time in routes:
        adj_list[city_1].append((city_2, time))
        adj_list[city_2].append((city_1, time))

    min_heap = [(0, origin)]
    shortest_times = {origin: 0}

    while min_heap:
        cur_time, city = heapq.heappop(min_heap)
        if cur_time > shortest_times[city]:
            continue

        for next_city, travel_time in adj_list[city]:
            stopover_time = 0 if city == origin else 1
            new_time = cur_time + travel_time + stopover_time

            if new_time <= k and new_time < shortest_times.get(next_city, float("inf")):
                shortest_times[next_city] = new_time
                heapq.heappush(min_heap, (new_time, next_city))

    return len(shortest_times) - 1


if __name__ == "__main__":
    routes = [
        ("Boston", "New York", 4),
        ("New York", "Philadelphia", 2),
        ("Boston", "Newport", 1.5),
        ("Washington, D.C.", "Harper's Ferry", 1),
        ("Boston", "Portland", 2.5),
        ("Philadelphia", "Washington, D.C.", 2.5),
    ]

    print(vacation_destinations(routes, "New York", 5))  # Expected: 2
    print(vacation_destinations(routes, "New York", 7))  # Expected: 4
    print(vacation_destinations(routes, "New York", 8))  # Expected: 6
