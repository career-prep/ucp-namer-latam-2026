#Time taken: 35 mins
#time complexity: O(V+E) numebr of edges and vertices visited
"""
Given an origin city, a maximum travel time k, and pairs of destinations
 that can be reached directly from each other with corresponding travel
   times in hours, return the number of destinations within k hours of the origin.
     Assume that having a stopover in a city adds an hour of travel time.
"""

"""
lets build that graph first

eg input
Input: [("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5), 
("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

portland
 |
 |
 2.5
 |
 |
boston --4-- newyork --2-- philadelphia --2.5-- washdc --1-- harper ferry
 |
 |
 1.5
 |
 |
 newport
"""

#algo:
"""
first: build an adj_list with key being "from" city and value being list of tuple("To", hours)
initial approach: to use the dfs and visit nei_cities of origin city and while doing dfs calc the cost if cost > k end the loop
and go to the next neighbour
"""
#code:
from collections import defaultdict
def vacationDestinations(city_edge_list, origin_city, k):
    city_adj_list = defaultdict(list)
    visited = set()
    resDestinations = []
    cost = 0
    for city1, city2, hours in city_edge_list:
        city_adj_list[city1].append((city2, hours))
        city_adj_list[city2].append((city1, hours))

    dfs(city_adj_list, origin_city, k, visited, resDestinations, cost)

    # print (city_adj_list)
    return resDestinations

def dfs(city_adj_list, origin_city, k, visited, resDestinations, cost):
    visited.add(origin_city)
    for nei_city in city_adj_list[origin_city]:
        if nei_city[0] not in visited:
            new_cost = cost+ nei_city[1] #logic to add 1 for visted detiantion in recursive call
            if new_cost <= k:
                resDestinations.append(nei_city[0])
            dfs(city_adj_list, nei_city[0], k, visited, resDestinations, new_cost+1)

print(vacationDestinations(
    [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), 
    ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],
    "New York",
    8
))