# Time complexity: O(T + R), T = # of towns, R = # of roads
# Space complexity: O(T + R)

# Technique: Generic traversal
from collections import deque

# takes a list of towns and a list of roads
def RoadNetworks(towns, roads):
    adjacencyList = {}

    for townA, townB in roads:
        if townA not in adjacencyList: adjacencyList[townA] = set()
        if townB not in adjacencyList: adjacencyList[townB] = set()
        adjacencyList[townA].add(townB)
        adjacencyList[townB].add(townA)

    visited = set()
    numNetworks = 0

    # disconnected graph
    for town in adjacencyList:
        if town not in visited:
            numNetworks += 1

            q = deque([town])
            visited.add(town)

            while q:
                curr = q.popleft()

                for neighbor in adjacencyList.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

    return numNetworks

if __name__ == "__main__":
    # input = (towns, roads)
    input1 = (["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 
    [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")])

    input2 = (["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")])

    input3 = (["Montreal"], [])

    inputs = [input1, input2, input3]
    for i in inputs:
        towns, roads = i
        print(RoadNetworks(towns, roads))

# ~ time spent: 20 minutes