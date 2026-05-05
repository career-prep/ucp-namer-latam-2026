# Data Structure: Graph
# Algorithm: Depth-first search
# Time Complexity: O(V + E)
# Space Complexity: O(V)

def road_networks(towns, roads):
    # Build graph
    graph = {t: [] for t in towns}
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

    # Count connected components with at least one edge
    for town in towns:
        if town not in visited and graph[town]:
            dfs(town)
            count += 1

    return count


# Time Taken: 16 mins 02 secs

# Test Cases
towns1 = ["Skagway","Juneau","Gustavus","Homer","Port Alsworth","Glacier Bay","Fairbanks","McCarthy","Copper Center","Healy","Anchorage"]
roads1 = [("Anchorage","Homer"),("Glacier Bay","Gustavus"),("Copper Center","McCarthy"),
          ("Anchorage","Copper Center"),("Copper Center","Fairbanks"),("Healy","Fairbanks"),("Healy","Anchorage")]
print(road_networks(towns1, roads1))

towns2 = ["Kona","Hilo","Volcano","Lahaina","Hana","Haiku","Kahului","Princeville","Lihue","Waimea"]
roads2 = [("Kona","Volcano"),("Volcano","Hilo"),("Lahaina","Hana"),("Kahului","Haiku"),
          ("Hana","Haiku"),("Kahului","Lahaina"),("Princeville","Lihue"),("Lihue","Waimea")]
print(road_networks(towns2, roads2))

# Edge Cases
print(road_networks([], []))
print(road_networks(["A","B"], []))
print(road_networks(["A","B"], [("A","B")]))