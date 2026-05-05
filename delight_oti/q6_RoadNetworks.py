def RoadNetwork(towns, roads):

    graph = {}

    for town in towns:
        graph[town] = []
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    networks = 0

    for town in towns:

        if town not in visited and len(graph[town]) > 0:
            networks += 1

            stack = [town]

            while stack:
                current = stack.pop()

                if current in visited:
                    continue

                visited.add(current)

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    return networks

# towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
#  "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 
# roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
# ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]

# Output = 2

# towns = ["Skagway", "Juneau", "Gustavis"]
# roads = []

# output = 0

# print(RoadNetwork(towns, roads))

# 40