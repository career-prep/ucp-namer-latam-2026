# Graph Depth-first Search
# O(V + E) Time Complexity where V is the number of towns and E is the number of roads (From the DFS and from building the adjacency list)
# O(V + E) Space Complexity where V is the number of towns and E is the number of roads (From building the adjacency list)
# Given a list of towns and a list of pairs representing roads between towns, return the number of road networks.


def RoadNetworks(towns, roads):

    # If we have no towns, or the towns are not connected by any roads, or both, then we have zero road networks
    if not towns or not roads:
        return 0
    

    # My intuition is as follows:
    # This is most likely a graph problem. The towns are nodes and the roads are edges.
    # Since you can go in both directions on a road, these edges are undirected, which means we cannot do topological sort.
    # This leaves my only option to being graph traversal.

    # My approach will be to first create an adjacency list of the towns and roads.
    # Then I will create a set to hold which towns we have already visited.
    # Next I will loop through each town, for any town we have not visited, run a dfs to explore the entire road network
    # Inside the dfs, I will add any new town to the visited set and only recursively call dfs on towns we have not already visted
    # Once the dfs finishes, I can add 1 to our network count, only if the town we are on is not isolated
    # Once the loop is done, we should have successfully counted all road networks





    # 1. Create Adjacency List
    graph = {town: [] for town in towns}

    # Populate the graph
    for town1, town2 in roads:
        graph[town1].append(town2)
        graph[town2].append(town1) # Because this graph is undirected



    
    # 2. Keep track of which towns we have already visted
    visited = set()
    networks = 0


    # Helper Recursive DFS
    def dfs(town):
        visited.add(town)

        for neighbor in graph[town]:
            if neighbor not in visited:
                dfs(neighbor)




    # 3. Loop through each town and visit all towns inside each roadnetwork and count the total amount of different road networks
    for town in towns:
        if town not in visited:
            dfs(town)
            
            # Isolated towns have no road networks, so we should only increase the network count if a town has roads connecting it to other towns
            if graph[town]:
                networks += 1



    return networks








# 31 minutes



# Test Cases
towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]

towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), 
          ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]

towns3 = ["Lebron", "Uber", "Cbum", "Neymar"]
roads3 = [("Lebron", "Neymar")]

towns4 = ["Elbaf"]
roads4 = []



print(RoadNetworks(towns1, roads1))
print(RoadNetworks(towns2, roads2))

# My Added Test Cases
print(RoadNetworks(towns3, roads3))
print(RoadNetworks(towns4, roads4))

    

