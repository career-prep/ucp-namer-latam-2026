# Time Taken: 15 minutes
# Time Complexity: O(V+E)
# Space Complexity: O(V+E)
# Algorithm: DFS (but BFS can probably be used but will be more complicated from what I think)

from collections import defaultdict 

def road_networks(towns, roads) -> int:
    """
    Given a list of towns and roads between towns, return the number of
    separate road networks.
    """
    adj_list = defaultdict(list) 

    visited = set()
    for v, e in roads:
        adj_list[v].append(e) 
        adj_list[e].append(v) 

    def dfs(road):
        if road in visited:
            return 
        visited.add(road)
        for e in adj_list[road]:
            dfs(e) 
        return 
    count = 0  
    for r in adj_list.keys():
        if r in visited:
            continue 
        else:
            dfs(r)
            count += 1
    return count
         

    


if __name__ == "__main__":
    towns_1 = [
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
    roads_1 = [
        ("Anchorage", "Homer"),
        ("Glacier Bay", "Gustavus"),
        ("Copper Center", "McCarthy"),
        ("Anchorage", "Copper Center"),
        ("Copper Center", "Fairbanks"),
        ("Healy", "Fairbanks"),
        ("Healy", "Anchorage"),
    ]

    towns_2 = [
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
    roads_2 = [
        ("Kona", "Volcano"),
        ("Volcano", "Hilo"),
        ("Lahaina", "Hana"),
        ("Kahului", "Haiku"),
        ("Hana", "Haiku"),
        ("Kahului", "Lahaina"),
        ("Princeville", "Lihue"),
        ("Lihue", "Waimea"),
    ]

    print(road_networks(towns_1, roads_1))  # Expected: 2
    print(road_networks(towns_2, roads_2))  # Expected: 3