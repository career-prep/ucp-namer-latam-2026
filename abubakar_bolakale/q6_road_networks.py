# Data structure: Graph (adjacency list)
# Algorithm: Breadth-first search (connected components)

from collections import deque


def road_network_count(towns, roads):
    adj = {t: [] for t in towns}
    for a, b in roads:
        adj[a].append(b)
        adj[b].append(a)
    seen = set()
    groups = 0
    for t in towns:
        if t in seen:
            continue
        groups += 1
        seen.add(t)
        q = deque([t])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return groups


if __name__ == "__main__":
    roads_ak = [
        ("Anchorage", "Homer"),
        ("Glacier Bay", "Gustavus"),
        ("Copper Center", "McCarthy"),
        ("Anchorage", "Copper Center"),
        ("Copper Center", "Fairbanks"),
        ("Healy", "Fairbanks"),
        ("Healy", "Anchorage"),
    ]
    ak_on_graph = sorted({x for ab in roads_ak for x in ab})
    print("=== Alaska roads only (spec-style count 2) ===")
    print(" ", road_network_count(ak_on_graph, roads_ak))

    print("=== Alaska all 11 towns (isolated towns extra components) ===")
    ak_all = [
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
    print(" ", road_network_count(ak_all, roads_ak))

    hi = [
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
    roads_hi = [
        ("Kona", "Volcano"),
        ("Volcano", "Hilo"),
        ("Lahaina", "Hana"),
        ("Kahului", "Haiku"),
        ("Hana", "Haiku"),
        ("Kahului", "Lahaina"),
        ("Princeville", "Lihue"),
        ("Lihue", "Waimea"),
    ]
    print("=== Hawaii (spec count 3) ===")
    print(" ", road_network_count(hi, roads_hi))

    print("=== No roads ===")
    print(" ", road_network_count(["a", "b", "c"], []))

    print("=== One town ===")
    print(" ", road_network_count(["solo"], []))

    print("=== Ring of 4 ===")
    print(" ", road_network_count([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4), (4, 1)]))


# Time complexity: O(V + E)
# Space complexity: O(V + E)
# Time spent: 30 minutes
