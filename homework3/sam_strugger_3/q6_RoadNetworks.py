# O(V + E) time and space
# Data structure is a graph. Used generic traversal (DFS) to count connected components.

def roadNetworks(towns, roads):
    # Plan
    # Make adjaceny set graph of roads
    # Traverse graph with dfs 
    # when a new town is found count +=1 and dfs on import 
    # dfs adds to visited since it is a part of road Network
    # repeat
        
    graph = {}

    for t1, t2 in roads:
        if t1 not in graph:
            graph[t1] = []
        if t2 not in graph:
            graph[t2] = []

        graph[t1].append(t2)
        graph[t2].append(t1)

    visited = set()
    count = 0
        
    def dfs(t):
        if t not in visited:
            visited.add(t)
            for destination in graph[t]:
                dfs(destination)

    for town in graph:
        if town not in visited:
            count+=1
            dfs(town)

    return count    

            
        


    

towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
test1 = roadNetworks(towns1, roads1)
print(test1)

towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
test2 = roadNetworks(towns2, roads2)
print(test2)

# 30 minutes
