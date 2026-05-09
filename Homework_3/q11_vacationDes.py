# Question 11: VacationDestinations
#
# Given an origin city, a maximum travel time k, and pairs of destinations that can be reached
# directly from each other with corresponding travel times in hours, return the number of
# destinations within k hours of the origin. Assume that having a stopover in a city adds
# an hour of travel time.
#
# Examples:
#
# Input: [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5),
#          ("Washington D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5),
#          ("Philadelphia", "Washington D.C.", 2.5)]
#
# Origin = "New York", k=5
# Output: 2 (["Boston", "Philadelphia"])
#
# Origin = "New York", k=7
# Output: 4 (["Boston", "Philadelphia", "Washington D.C.", "Newport"])
#
# Origin = "New York", k=8
# Output: 6 (["Boston", "Philadelphia", "Washington D.C.", "Newport", "Harper's Ferry", "Portland"])
from collections import defaultdict
def vacation_destinations(trips, origin, k):
    graph = defaultdict(list)
    for city1, city2, time in trips:
        graph[city1].append((city2, time))
        graph[city2].append((city1, time))

    reachable = set()

    def dfs(city, time_spent, path):
        for neighbor, travel_time in graph[city]:
            if neighbor in path:
                continue
            arrival = time_spent + travel_time
            if arrival <= k:
                reachable.add(neighbor)
                path.add(neighbor)
                dfs(neighbor, arrival + 1, path)
                path.remove(neighbor)

    dfs(origin, 0, {origin})
    return len(reachable)



trips2 = [
    ("Los Angeles", "San Francisco", 6),
    ("San Francisco", "Seattle", 3),
    ("Seattle", "Portland", 2),
    ("Los Angeles", "Las Vegas", 4),
    ("Las Vegas", "Phoenix", 2),
]

print(vacation_destinations(trips2, "Los Angeles", 7))
print(vacation_destinations(trips2, "Los Angeles", 11))
print(vacation_destinations(trips2, "Los Angeles", 14))


