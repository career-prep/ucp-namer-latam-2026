#Time Complexity: O(N + E)
#Space Complexity: O(N + E)
#Technique: Graph DFS

from collections import defaultdict

def count_road_networks(towns, roads):
    graph = defaultdict(list)

    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for town in graph:
        if town not in visited:
            dfs(town)
            count += 1

    return count

def test():
    towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", 
              "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]

    roads1 = [
        ("Anchorage", "Homer"),
        ("Glacier Bay", "Gustavus"),
        ("Copper Center", "McCarthy"),
        ("Anchorage", "Copper Center"),
        ("Copper Center", "Fairbanks"),
        ("Healy", "Fairbanks"),
        ("Healy", "Anchorage")
    ]

    print(count_road_networks(towns1, roads1), "Expected: 2")


    towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", 
              "Kahului", "Princeville", "Lihue", "Waimea"]

    roads2 = [
        ("Kona", "Volcano"),
        ("Volcano", "Hilo"),
        ("Lahaina", "Hana"),
        ("Kahului", "Haiku"),
        ("Hana", "Haiku"),
        ("Kahului", "Lahaina"),
        ("Princeville", "Lihue"),
        ("Lihue", "Waimea")
    ]

    print(count_road_networks(towns2, roads2), "Expected: 3")


test()

#time: 38 min
