from collections import defaultdict
def roadNetworks(towns, connectedTowns):
    """
    idea:
    Build an undirected graph from the road pairs.
    Then iterate through each town. If a town has at least one road and has not
    been visited yet, start a DFS from that town to mark every town in the same
    connected component. Each DFS represents one road network.

    Time complexity: O(T + R)
    Space complexity: O(T + R)
    """

    graph = defaultdict(set)
    visited = set()
    ans = 0

    for u, v in connectedTowns:
        graph[u].add(v)
        graph[v].add(u)
    
    for town in towns:
        if town in visited or town not in graph:
            continue 
        stack = [town]
        ans += 1
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            for nei in graph[cur]:
                if nei not in visited:
                    stack.append(nei)

    return ans


if __name__ == "__main__":
    example1_towns = [
        "Skagway",
        "Juneau",
        "Gustavus",
        "Homer",
        "Port Alsworth",
        "Glacier Bay",
        "Fairbanks",
        "McCarthy",
        "Copper Center",
        "Healy",
        "Anchorage",
    ]
    example1_roads = [
        ("Anchorage", "Homer"),
        ("Glacier Bay", "Gustavus"),
        ("Copper Center", "McCarthy"),
        ("Anchorage", "Copper Center"),
        ("Copper Center", "Fairbanks"),
        ("Healy", "Fairbanks"),
        ("Healy", "Anchorage"),
    ]

    example2_towns = [
        "Kona",
        "Hilo",
        "Volcano",
        "Lahaina",
        "Hana",
        "Haiku",
        "Kahului",
        "Princeville",
        "Lihue",
        "Waimea",
    ]
    example2_roads = [
        ("Kona", "Volcano"),
        ("Volcano", "Hilo"),
        ("Lahaina", "Hana"),
        ("Kahului", "Haiku"),
        ("Hana", "Haiku"),
        ("Kahului", "Lahaina"),
        ("Princeville", "Lihue"),
        ("Lihue", "Waimea"),
    ]

    print(roadNetworks(example1_towns, example1_roads))  # Expected: 2
    print(roadNetworks(example2_towns, example2_roads))  # Expected: 3
