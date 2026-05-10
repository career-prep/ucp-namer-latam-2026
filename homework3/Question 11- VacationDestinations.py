#time: 40 minutes
# BFS 
def VacationDestinations(source, k, edges):
    graph = {}
    for src, dst, travel_time in edges:
        if src not in graph:
            graph[src] = set()
        if dst not in graph:
            graph[dst] = set()
    
    for src, dst, travel_time in edges:
        graph[src].add((dst, travel_time))
        graph[dst].add((src, travel_time))
    
    q = [(source, 0)]
    visited = set()
    count = 0
    while q:
        city, current_time = q.pop(0)

        if city in visited:
            continue
        visited.add(city)

        if current_time > k:
            continue

        if current_time <= k and city != source:
            count += 1
        
        for neighbor, travel_time in graph[city]:
            next_time = current_time + travel_time + 1
            q.append((neighbor, next_time))

    return count

edges = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), 
        ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), 
        ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

print(VacationDestinations("New York", 5, edges))   
print(VacationDestinations("New York", 7, edges))   
print(VacationDestinations("New York", 8, edges))  