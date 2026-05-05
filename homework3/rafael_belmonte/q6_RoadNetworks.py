# Data Structure: Graph (adjacency list)
# Algorithm: Generic traversal — count connected components.
#
# Treat each town as a node and each road as an undirected edge. Run a traversal
# from every unvisited node; each launch counts as one connected component
# (one "road network"). A town with no roads is NOT counted (per the problem
# statement: "a state in which none of the towns are connected by roads has 0").
#
# Time complexity:  O(V + E)
# Space complexity: O(V + E)

from collections import defaultdict, deque


def road_networks(towns, roads):
    graph = defaultdict(set)
    has_road = set()
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)
        has_road.add(a)
        has_road.add(b)

    visited = set()
    networks = 0
    for town in towns:
        if town in visited or town not in has_road:
            continue
        networks += 1
        queue = deque([town])
        visited.add(town)
        while queue:
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
    return networks


# test cases
if __name__ == "__main__":
    towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
              "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center",
              "Healy", "Anchorage"]
    roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
              ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"),
              ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"),
              ("Healy", "Anchorage")]
    assert road_networks(towns1, roads1) == 2

    towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku",
              "Kahului", "Princeville", "Lihue", "Waimea"]
    roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"),
              ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"),
              ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    assert road_networks(towns2, roads2) == 3

    # no roads at all -> 0
    assert road_networks(["A", "B", "C"], []) == 0
    # single road
    assert road_networks(["A", "B", "C"], [("A", "B")]) == 1

    print("yay!!")

# Time spent: ~15 minutes
