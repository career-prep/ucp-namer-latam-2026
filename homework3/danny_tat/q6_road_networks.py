from collections import deque
# Data Structure: Graph, Hashmap, Queue
# Algorithm: Breadth-First Search
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Given a list of towns and road pairs between towns, return the number of road networks
# (connected components with at least one road).


def roadNetworks(towns, roads):
    graph = {town: [] for town in towns}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    networks = 0

    def bfs(start):
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for town in towns:
        if town not in visited and graph[town]:
            bfs(town)
            networks += 1

    return networks


# Testing:
towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay",
          "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
          ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
          ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print(roadNetworks(towns1, roads1))  # 2

towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku",
          "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [("Kona", "Volcano"), ("Lahaina", "Hilo"), ("Kahului", "Haiku"),
          ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"),
          ("Lihue", "Waimea")]
print(roadNetworks(towns2, roads2))  # 3

# Time: 24 min
