# Question 6: RoadNetworks

# Data Structure: Graph (undirected)
# Algorithm: DFS — count connected components with size >= 2
# (isolated towns with no roads are not counted as a network)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)


def roadNetworks(towns, roads):
    graph = {town: [] for town in towns}
    for a, b in roads:
        if a in graph:
            graph[a].append(b)
        if b in graph:
            graph[b].append(a)

    visited = set()
    count = 0

    def dfs(town, component):
        visited.add(town)
        component.append(town)
        for neighbor in graph.get(town, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for town in towns:
        if town not in visited:
            component = []
            dfs(town, component)
            if len(component) > 1:
                count += 1

    return count


# --- Tests ---

# Test 1 from task
towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
          "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
          ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
          ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print("Test 1:", roadNetworks(towns1, roads1))  # 2

# Test 2 from task
towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana",
          "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"),
          ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"),
          ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print("Test 2:", roadNetworks(towns2, roads2))  # 3

# Test 3: all isolated
towns3 = ["A", "B", "C"]
print("Test 3 (no roads):", roadNetworks(towns3, []))  # 0

# Test 4: all connected
towns4 = ["A", "B", "C"]
roads4 = [("A", "B"), ("B", "C")]
print("Test 4 (one network):", roadNetworks(towns4, roads4))  # 1

# Spent a total of 25 mins on this question
