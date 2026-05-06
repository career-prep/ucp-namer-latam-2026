# Algorithm: DFS to count connected components in an undirected graph
# An isolated town with no roads does not count as a road network.
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)


def roadNetworks(towns, roads):
    graph = {town: set() for town in towns}
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    count = 0
    for town in towns:
        if town in visited:
            continue
        if not graph[town]:  # isolated town, not part of any network
            continue
        count += 1
        stack = [town]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return count


print("RoadNetworks Results:")

towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
         "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
          ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
          ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"),
          ("Healy", "Anchorage")]
print(roadNetworks(towns1, roads1))

towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku",
          "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"),
          ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"),
          ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(roadNetworks(towns2, roads2))

print(roadNetworks(["A", "B", "C"], []))
print(roadNetworks(["A", "B", "C"], [("A", "B"), ("B", "C")]))
