# Data Structure: Graph
# Algorithm: DFS
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import defaultdict

def roadNetworks(towns, roads):
    graph = defaultdict(set)
    for town in towns:
        graph[town]

    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    count = 0
    def dfs(town):
        visited.add(town)
        for neighbor in graph[town]:
            if neighbor not in visited:
                dfs(neighbor)

    for town in towns:
        if town not in visited and len(graph[town]) > 0:
            dfs(town)
            count += 1

    return count


towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
          "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [
    ("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
    ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
    ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")
]
print(roadNetworks(towns1, roads1)) 

towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku",
          "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [
    ("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"),
    ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"),
    ("Princeville", "Lihue"), ("Lihue", "Waimea")
]
print(roadNetworks(towns2, roads2)) 

# Time spent: 45 minutes
