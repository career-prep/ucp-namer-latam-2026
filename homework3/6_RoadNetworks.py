# Data Structure: Graph (Adjacency List)
# Algorithm: Depth-First Search (DFS)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import defaultdict

def countRoadNetworks(towns, roads):
    if not towns:
        return 0
        
    adj = defaultdict(list)
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = set()
    networks = 0
    
    def dfs(town):
        visited.add(town)
        for neighbor in adj[town]:
            if neighbor not in visited:
                dfs(neighbor)
                
    for town in towns:
        if town not in visited:
            networks += 1
            dfs(town)
            
    return networks

def main():
    towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
    roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    print(f"Test Case 1 - Result: {countRoadNetworks(towns1, roads1)}")

    towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Haiku", "Kahului"), ("Hana", "Haiku"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    print(f"Test Case 2 - Result: {countRoadNetworks(towns2, roads2)}")

if __name__ == "__main__":
    main()

# Time Spent: 25 minutes