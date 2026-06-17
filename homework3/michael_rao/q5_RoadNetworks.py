# Data structure: Graph - DFS
# Time: O(V + E)
# Space: O(V + E)


def count_road_networks(towns, roads):
    towns_set = set(towns)
    graph = {}
    for a, b in roads:
        if a not in towns_set or b not in towns_set:
            continue
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    networks = 0

    for town in graph:
        if town in visited:
            continue
        networks += 1
        stack = [town]
        visited.add(town)
        while stack:
            cur = stack.pop()
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
    return networks


towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print("Correct:", 2)
print("Output: ", count_road_networks(towns, roads))
print()

towns = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Hana", "Kahului"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Volcano", "Volcano"), ("Lihue", "Princeville"), ("Lihue", "Waimea")]
print("Correct:", 3)
print("Output: ", count_road_networks(towns, roads))
print()

print("Correct:", 0)
print("Output: ", count_road_networks([], []))
print()

# time taken: 25 min
