"""
Input: ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
 "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 

[("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"),
 ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]

output: 2 
networks are: (Networks are Gustavus-Glacier Bay and Anchorage-Fairbanks-McCarthy-Copper Center-Homer-Healy)
"""

"""
given: 1.we are given the towns as array

2. an array of networks that exists

return: the total number of road networks2

"Anchorage" ------- "Homer"   
| |
| |
| |
| "Copper Center" -------- "McCarthy"
|  |
|  |
|  |
|"Fairbanks"
|  |
|   |
|   |
|----"healy"

"Glacier Bay" ----------  "Gustavus"

OUTPUT: we have Two disticnt tree, so the output is 2



EG2

Input: ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"],

 [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), 
 ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]

 
make the network:

"Kona"--------"Volcano" ------- "Hilo"

"Lahaina"------ "Hana"
    |               |
    |               |
    |               |
Kahului" ------ "Haiku"


"Princeville" ------ "Lihue" ------ "waimea"

OUTPUT: we have 3 distinct trees, so the output is 3

"""


"""
logic:
 1.first we build a adj_list to understand what towns are connected to what towns
 2.then we conduct a depth first search from any random town to see what other town can be visted from that same networks
   and we also keep track of each visited town and increase the counter by 1 initially
 3. once we are done with dfs we iteratre over the adj_list to check if any town is missed
    if this mised town has neighbours, it means there exist another networks so we increase the count
    elif this town does not have neighbours we dont increase the count becuase there exist a town which can not be reached by any network
 4. return count
"""
from collections import defaultdict 

def roadNetwork(towns, network):
    network_list = defaultdict(list)
    #assuming road networks are undirected
    for town1, town2 in network:
        network_list[town1].append(town2)
        network_list[town2].append(town1)
    
    seen_towns = set()
    seen_towns.add(towns[0])
    if network_list[towns[0]] == []:
        count = 0
    else:
        count = 1
    dfs(towns[0], network_list, seen_towns)
    
    
    for town in network_list:
        if town not in seen_towns:
            if network_list[town] != []:
                count += 1
                dfs(town, network_list, seen_towns)

    count2 = 0
    for town in network_list:
        if network_list[town] == []:
            count2 += 1

    if len(towns) == count2:
        return 0
    
    return count


def dfs(town, network_list, seen_towns):
    seen_towns.add(town)
    for nei_town in network_list[town]:
        if nei_town not in seen_towns:
            dfs(nei_town, network_list, seen_towns)


print(roadNetwork(["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
                  , [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), 
                    ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]))

print(roadNetwork(["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
 "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
                  , [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"),
 ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]))
