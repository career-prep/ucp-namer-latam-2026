# spent 40 minutes
# dfs
# TC - O(V+E)
# SC - O(V+E)


def road_networks(towns: list[str], roads: list[tuple[str, str]]) -> int:
    # build undirected graph from roads
    graph = {}
    for town1, town2 in roads:
        if town1 in graph:
            graph[town1].append(town2)
        else: 
            graph[town1] = [town2]
        if town2 in graph:
            graph[town2].append(town1)
        else:
            graph[town2] = []
        
    visited = set() # track which towns have been visited
    count = 0
    
    def dfs(town):
        # start from `town` and visit all connected towns
        stack = [town]
        visited.add(town)
        
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    
                    
    # will skip nodes with no edges
    for town in graph:
        if town not in visited:
            dfs(town)
            count += 1
        
    return count
    
    
    
if __name__ == "__main__":
    # test 1
    town1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
    road1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    print("Expected: 2")
    print("Actual  :", road_networks(town1, road1))
    
    # test 2
    town2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    road2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    print("Expected: 3")
    print("Actual  :", road_networks(town2, road2))