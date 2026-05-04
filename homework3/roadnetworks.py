# Data Structure: Graph + DFS (generic traversal)
# Technique: Undirected adjacency list, count connected components via DFS
# Time Complexity: O(V + E) where V = towns, E = roads
# Space Complexity: O(V + E) for the graph + visited set

def roadNetworks(towns, roads):
    # build undirected adjacency list
    graph = {town: [] for town in towns}
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(town):
        visited.add(town)
        for neighbor in graph[town]:
            if neighbor not in visited:
                dfs(neighbor)

    for town in towns:
        # only count as a network if the town has at least one road
        if town not in visited and graph[town]:
            count += 1
            dfs(town)

    return count


# Test 1: Alaska example -> 2 networks
towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
          "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
          ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
          ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print(roadNetworks(towns1, roads1))   # 2

# Test 2: Hawaii example -> 3 networks
towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku",
          "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"),
          ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"),
          ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(roadNetworks(towns2, roads2))   # 3

# Test 3: all towns isolated (no roads) -> 0
towns3 = ["A", "B", "C"]
roads3 = []
print(roadNetworks(towns3, roads3))   # 0

# Test 4: all towns in one network -> 1
towns4 = ["A", "B", "C"]
roads4 = [("A", "B"), ("B", "C")]
print(roadNetworks(towns4, roads4))   # 1

# Test 5: two separate pairs -> 2
towns5 = ["A", "B", "C", "D"]
roads5 = [("A", "B"), ("C", "D")]
print(roadNetworks(towns5, roads5))   # 2

# Time spent: ~35 minutes