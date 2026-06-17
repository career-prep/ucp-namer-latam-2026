graph = {}
def RoadBlocks(towns, roads):
    for town, road in roads:
        graph[town] = set()
        graph[road] = set()
    
    for town, road in roads:
        graph[town].add(road)
        graph[road].add(town)

    visited = set()
    networks = 0

    for node in graph:
        if node not in visited and graph[node]:
            networks += 1
            q = [node]
            while q:
                current = q.pop(0)
                if current in visited:
                    continue
                visited.add(current)
                for neighbor in graph[current]:
                    q.append(neighbor)
    return networks

towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", 
        "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]

roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), 
        ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), 
        ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), 
        ("Healy", "Anchorage")]

print(RoadBlocks(towns, roads))

