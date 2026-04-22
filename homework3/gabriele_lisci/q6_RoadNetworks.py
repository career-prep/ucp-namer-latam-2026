# Runtime: O(V + E) V is the # of towns, E is the # of roads
# Space complexity: O(V) # not including the graph itself
# Data Structure: Graph
# Algorithm: BFS

import collections
def roadNetworks(towns, roads):
    graph = {}
    for town in towns:
        graph[town] = []
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    visited = set()
    roadNetworks = 0
    for town in towns:
        if town not in visited:
            q = collections.deque()
            q.append(town)
            visited.add(town)
            currSize = 0
            while q:
                curr = q.popleft()
                currSize += 1
                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            if currSize > 1:
                roadNetworks += 1
    return roadNetworks

towns1 =  ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print(roadNetworks(towns1, roads1))

towns2 =  ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 =  [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(roadNetworks(towns2, roads2))

print(roadNetworks([],[]))

towns3 = ["A", "B", "C"]
print(roadNetworks(towns3, []))
roads3 = [("A", "B"), ("B", "C"), ("C", "A")]
print(roadNetworks(towns3, roads3))


# Time Spent: 20:00
