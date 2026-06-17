# Technique: Disjoint Set Union (DSU) or Graph Connected Components (BFS/DFS)

def roadNetworks(towns, roads): # Time Complexity: O(V + E), Space Complexity: O(V + E)
    # 1. Build an adjacency list representation of the road network
    adj = {town: [] for town in towns}
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = set()
    network_count = 0

    # 2. Define traversal to mark all towns in a single connected network
    def traverse(start_town):
        stack = [start_town]
        visited.add(start_town)
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    # 3. Iterate through all towns; each unvisited town starts a new network
    for town in towns:
        if town not in visited:
            network_count += 1
            traverse(town)
            
    return network_count

class Test:
    def run_tests(self):
        # 1. Test Case: Alaska Example (2 networks)
        towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
        roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
        assert roadNetworks(towns1, roads1) == 2
        
        # 2. Test Case: Hawaii Example (3 networks)
        towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
        roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
        assert roadNetworks(towns2, roads2) == 3

        print("RoadNetworks tests passed")

if __name__ == "__main__":
    tester = Test()
    tester.run_tests()

# Time complexity: O(V + E) where V is number of towns and E is number of roads.
# Space complexity: O(V + E) for the adjacency list and visited set.