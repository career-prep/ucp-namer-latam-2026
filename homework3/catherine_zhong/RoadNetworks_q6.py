#time complexity: O(nm)
#data structure/algorithm: DFS

def RoadNetworks(towns, roads):
    graph = {town: [] for town in towns}
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    networks = 0

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for i in graph[curr]:
                    stack.append(i)
    
    for town in towns:
        if town not in visited:
            if len(graph[town]) > 0:
                dfs(town)
                networks += 1

    return networks


#test cases
#0 road networks
towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
roads = []
print(f"no road networks: {RoadNetworks(towns,roads)}")

#1 road network with one town without roads
towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay"]
roads = [["Skagway", "Juneau"],["Juneau", "Gustavus"],["Gustavus", "Homer"],["Homer", "Port Alsworth"]]
print(f'one road network: {RoadNetworks(towns,roads)}')

#multiple road networks
towns = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
roads = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(f'multiple road network: {RoadNetworks(towns,roads)}')
#time spent: 25min