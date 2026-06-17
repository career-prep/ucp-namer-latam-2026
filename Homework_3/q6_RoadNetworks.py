# Question 6: RoadNetworks
#
# In some states, it is not possible to drive between any two towns because they are not connected
# to the same road network. Given a list of towns and a list of pairs representing roads between
# towns, return the number of road networks.
# (For example, a state in which all towns are connected by roads has 1 road network,
# and a state in which none of the towns are connected by roads has 0 road networks.)
#
# Examples:
#
# Input: ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay",
#         "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"],
#        [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"),
#         ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"),
#         ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
# Output: 2 (Networks are Gustavus-Glacier Bay and Anchorage-Fairbanks-McCarthy-Copper Center-Homer-Healy)
#
# Input: ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville",
#         "Lihue", "Waimea"],
#        [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"),
#         ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
#Output: 3 (Networks are Kona-Hilo-Volcano, Haiku-Kahului-Lahaina-Hana, and Lihue-Waimea-Princeville)

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

#Spent 50 mins