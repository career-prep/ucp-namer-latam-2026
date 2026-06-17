import heapq

# O(E log V) time and O(V + E) space complexity
# Data structure is a graph. I used Dijkstra's algorithm with a priority queue (min-heap).
def VacationDestinations(edges, originCity, k):
    # Plan
    # Build an adjacency list to represent the city connections
    # Use a priority queue to process cities in order of travel time
    # Apply the 1 hour stopover penalty if the city is not the origin
    # Count all cities reachable within k hours
    
    adjacencyList = {}

    for origin, destination, time in edges:
        if origin not in adjacencyList: 
            adjacencyList[origin] = []
        if destination not in adjacencyList: 
            adjacencyList[destination] = []
        
        adjacencyList[origin].append((destination, time))
        adjacencyList[destination].append((origin, time))

    priorityQueue = [(0, originCity)]
    minTravelTimes = {originCity: 0}
    
    while priorityQueue:
        currentTime, currentCity = heapq.heappop(priorityQueue)
        
        if currentTime > minTravelTimes.get(currentCity, float('inf')):
            continue
            
        if currentCity in adjacencyList:
            for neighborCity, travelTime in adjacencyList[currentCity]:
                stopoverPenalty = 1
                newTravelTime = currentTime + travelTime + stopoverPenalty

                if newTravelTime < k:
                    if neighborCity not in minTravelTimes or newTravelTime < minTravelTimes[neighborCity]:
                        minTravelTimes[neighborCity] = newTravelTime
                        heapq.heappush(priorityQueue, (newTravelTime, neighborCity))

    return len(minTravelTimes)


edges = [
    ("Boston", "New York", 4), 
    ("New York", "Philadelphia", 2), 
    ("Boston", "Newport", 1.5), 
    ("Washington, D.C.", "Harper's Ferry", 1), 
    ("Boston", "Portland", 2.5), 
    ("Philadelphia", "Washington, D.C.", 2.5)
]

test1 = VacationDestinations(edges, "New York", 5)
print(f"k=5: {test1}")

# this took me over an hour, still has some bugs I'm solving for. 
