# Method: DFS
# Space Complexity: O(N * M)
# Time Complexity: O(N * M)
# Total Time Taken: 30 mins

def RoadNetworks(towns, roads):
    graph = {}
# Create a graph list to show all possible towns you can get to from each town (undirected)
    for town1, town2 in roads:
        if town1 not in graph: graph[town1] = set()
        if town2 not in graph: graph[town2] = set()

        graph[town1].add(town2)
        graph[town2].add(town1)

    seen = set()
    roads = 0

# DFS function to explore the road that the town is connected to
    def explore(town):
        seen.add(town)
        for neighbor in graph.get(town, []):
            if neighbor not in seen:
                explore(neighbor)

# Explore each town
    for towns in graph:
        if towns not in seen:
            roads += 1

            explore(towns)
    return roads

towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print(RoadNetworks(towns, roads)) # Expected 2

towns = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(RoadNetworks(towns, roads)) # Expected 3

print(RoadNetworks([], [])) # Expected 0