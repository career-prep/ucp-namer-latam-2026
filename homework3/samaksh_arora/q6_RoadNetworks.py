# Road Networks
# Data Structure: Graph
# Algorithm: DFS (generic traversal)
# Time Complexity: O(T + R) where T is the number of towns and R is the number of roads
# Space Complexity: O(T + R) where T is the number of towns and R is the number of roads

def RoadNetworks(listOfTowns, listOfRoadPairs):
    townToNeighborsMap = {}

    for town in listOfTowns:
        townToNeighborsMap[town] = set()

    for townA, townB in listOfRoadPairs:
        townToNeighborsMap[townA].add(townB)
        townToNeighborsMap[townB].add(townA)

    setOfVisitedTowns = set()
    roadNetworkCount = 0


    def dfsMarkEntireNetwork(currentTown):
        setOfVisitedTowns.add(currentTown)
        for neighboringTown in townToNeighborsMap[currentTown]:
            if neighboringTown not in setOfVisitedTowns:
                dfsMarkEntireNetwork(neighboringTown)
    
    for currentTown in listOfTowns:
        if currentTown not in setOfVisitedTowns:
            if len(townToNeighborsMap[currentTown]) > 0:
                roadNetworkCount += 1
                dfsMarkEntireNetwork(currentTown)

    return roadNetworkCount

#Test Cases

towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
           "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
           ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
           ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print(RoadNetworks(towns1, roads1))  # expected: 2

towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku",
           "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"),
           ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"),
           ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(RoadNetworks(towns2, roads2))  # expected: 3