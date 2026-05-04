def network(towns,roads):
    #Building undirected adjacency list
    adj={town:[] for town in towns}
    for u,v in roads:
        adj[u].append(v)
        adj[v].append(u)
    visited=set()
    def dfs(town):
        visited.add(town)
        for nei in adj[town]:
            if nei not in visited:
                dfs(nei)
    networks=0
    for town in towns:
        if town not in visited:
            networks+=1
            dfs(town)
    return networks


towns2 = ["A", "B", "C", "D"]
roads2 = [("A", "B"), ("B", "C"), ("C", "D")]
print(network(towns2, roads2))

towns3 = ["A", "B", "C", "D"]
roads3 = []
print(network(towns3, roads3))

towns4 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads4 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(network(towns4, roads4))

#Time Complexity:O(V+E)
#Space Complexity:O(V+E)
