# spent 60 minutes
# dijkstra
# TC - O((V+E)*logV)
# SC - O(V+E)

import heapq

def vacationDestinations(directed_graph: list[tuple[str, str, int]], origin: str, k: int) -> int:
    # convert into undirected graph
    graph = {}
    for city1, city2, _ in directed_graph: # make empty lists for each city
        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []
    for city1, city2, dist in directed_graph: # add as undirected edges
        graph[city1].append( (city2, dist) )
        graph[city2].append( (city1, dist) )
        
    heap = [(0, origin)] # [(time, city)]
    best_time = {origin : 0} # graph of shortest times from origin to key  # {destination city : shortest time}

    while heap: 
        time_elapsed, city = heapq.heappop(heap)
        
        if time_elapsed > best_time.get(city, float('inf')): # shorter path exists -> skip
            continue
        
        for neighbor, dist in graph.get(city, []): # iterate through neighbors 
            # calculate time (+1 for stopover)
            new_time_elapsed = time_elapsed + dist + 1
            if new_time_elapsed-1 > k: # not enough time -> skip
                continue
            
            # only continue if this path is quicker 
            if neighbor not in best_time or new_time_elapsed < best_time[neighbor]:
                best_time[neighbor] = new_time_elapsed
                heapq.heappush(heap, (new_time_elapsed, neighbor))
                
    # count cities reachable within `k` excluding origin
    count = 0
    for city, time_elapsed in best_time.items():
        if city != origin and time_elapsed-1 <= k:
            count += 1
    return count
        


if __name__ == "__main__":
    input =  [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
    
    # test 1
    origin1 = "New York"
    k1 = 5
    print("Expected: 2")
    print("Actual  :", vacationDestinations(input, origin1, k1))
    
    # test 2
    origin2 = "New York"
    k2 = 7
    print("Expected: 4")
    print("Actual  :", vacationDestinations(input, origin2, k2))
    
    # test 3 
    origin3 = "New York"
    k3 = 8
    print("Expected: 6")
    print("Actual  :", vacationDestinations(input, origin3, k3))
