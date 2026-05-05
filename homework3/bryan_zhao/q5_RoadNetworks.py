# Data Structure: Graph
# Algorithm: Generical traversal
# Time Complexity: O(V + E) because we visit each town and each road exactly once
# Space Complexity: O(V + E) to store adjacency list and the seen set


from collections import defaultdict

def road_networks(towns, roads):
    graph = defaultdict(list)
    
    # Constructing the graphs only for towns with roads (undirected so append both entries)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    seen = set()
    network_count = 0

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in seen:
                seen.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        stack.append(neighbor)

    for town in list(graph.keys()):
        if town not in seen:
            network_count += 1
            dfs(town)

    return network_count

towns_1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads_1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]

towns_2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads_2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]

print(road_networks(towns_1, roads_1))
print(road_networks(towns_2, roads_2))

# Time Spent: 37 min