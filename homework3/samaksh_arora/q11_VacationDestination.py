# Vacation Destinations
# Data Structure: Graph
# Algorithm: Dijkstra's Algorithm
# Time Complexity: O((C + R) log C) where C is the number of cities and R is the number of routes
# Space Complexity: O(C + R) where C is the number of cities and R is the number of routes

import heapq

def vacationDestinations(listOfRoutes, originCity, maxTravelTimeK):
    cityToWeightedNeighborsMap = {}

    for cityA, cityB, travelTime in listOfRoutes:
        if cityA not in cityToWeightedNeighborsMap:
            cityToWeightedNeighborsMap[cityA] = set()
        if cityB not in cityToWeightedNeighborsMap:
            cityToWeightedNeighborsMap[cityB] = set()
        cityToWeightedNeighborsMap[cityA].add((cityB, travelTime))
        cityToWeightedNeighborsMap[cityB].add((cityA, travelTime))

    minHeap = [(0, originCity)]
    cityToShortestTravelTimeMap = {originCity: 0}

    while minHeap:
        currentTravelTime, currentCity = heapq.heappop(minHeap)

        if currentTravelTime > cityToShortestTravelTimeMap.get(currentCity, float('inf')):
            continue

        if currentCity not in cityToWeightedNeighborsMap:
            continue

        for neighboringCity, directTravelTime in cityToWeightedNeighborsMap[currentCity]:
            travelTimeThroughCurrentCity = currentTravelTime + directTravelTime + 1

            if travelTimeThroughCurrentCity < cityToShortestTravelTimeMap.get(neighboringCity, float('inf')):
                cityToShortestTravelTimeMap[neighboringCity] = travelTimeThroughCurrentCity
                heapq.heappush(minHeap, (travelTimeThroughCurrentCity, neighboringCity))

    reachableDestinationCount = 0
    for city, shortestTravelTime in cityToShortestTravelTimeMap.items():
        if city != originCity and shortestTravelTime <= maxTravelTimeK:
            reachableDestinationCount += 1

    return reachableDestinationCount



#  Test Cases
routes = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

print(vacationDestinations(routes, "New York", 5))   # expected: 2
print(vacationDestinations(routes, "New York", 7))   # expected: 4
print(vacationDestinations(routes, "New York", 8))   # expected: 6