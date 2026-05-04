from collections import defaultdict

def roadNetworks(towns, roads):
    graph = defaultdict(set)
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)
    
        
    visited = set()

    def dfs(town):
        visited.add(town)
        for neighbor in graph[town]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0

    for town in towns:
        if town not in visited:
            if graph[town]:
                count += 1
            dfs(town)

    return count

if __name__ == "__main__":

    towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
              "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
    roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
              ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
              ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    print("Test 1 (expect 2):", roadNetworks(towns1, roads1))

    towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana",
              "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"),
              ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"),
              ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    print("Test 2 (expect 3):", roadNetworks(towns2, roads2))
