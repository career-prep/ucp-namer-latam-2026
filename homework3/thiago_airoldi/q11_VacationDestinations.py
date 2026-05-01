# Graph Traversal - BFS with Priority Queue (Dijkstra's Algorithm)
# O((V + E)log(V)) Time Complexity
# O(V + E) Space Complexity
# Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each other with corresponding travel times in hours, 
# return the number of destinations within k hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

from q3_PriorityQueue import PriorityQueue

def VacationDestinations(connections, origin, k):

    if k <= 0 or not connections:
        return 0
    

    # 1. Create an adjacency list from the connections array
    # Note that the graph we are given is undirected because 'pairs of destinations that can be reached directly from each other'

    graph = {}

    for city1, city2, flightTime in connections:

        if city1 not in graph:
            graph[city1] = []

        if city2 not in graph:
            graph[city2] = []

        graph[city1].append((city2, flightTime))
        graph[city2].append((city1, flightTime))



    # 2. Create a distance hashmap which stores the shortest total flight time to each city from the origin
    distance = {}
    # Initialize it with origin
    distance[origin] = 0



    # 3. Now create a priority queue which stores (city, flightTime)
    # However since my priority queue from question 3 was implemented as a max heap, I really need to store (city, -1 * flightTime)
    # that way, the top element still has the shortest flight time.
    pq = PriorityQueue()
    # Initialize pq with the origin and it's flight time (which is zero because the distance from origin to itself is 0)
    pq.insert(origin, 0)


    

    # 4. Dijkstra's Loop (populate the distance hashmap)
    while len(pq.PQ) > 0: # While the priority queue is not empty...

        # Extract the element with the smallest cost
        currentCity, negCost = pq.top()
        pq.remove() # Removes the element we just extracted

        cost = -1 * negCost # Converts the cost back to normal


        # If the cost (flight time) we just got is greater than a cost we already have recorded for it, we can skip this path
        if cost > distance.get(currentCity, float('inf')): # the .get() returns infinity if the currentCity doesn't exist in the distance hashmap yet
            continue


        for neighbor, weight in graph[currentCity]:

            # Calculate the cost (flight time) for traveling to this neighbor from currentCity

            if currentCity == origin:
                newCost = cost + weight # No stopover penalty for coming from the origin
            else:
                newCost = cost + weight + 1 # + 1 hour for stopover


            if newCost < distance.get(neighbor, float('inf')):
                distance[neighbor] = newCost

                pq.insert(neighbor, -1 * newCost)







    # 5. Now that the distance hashmap is built, we can count which cities are reachable within k hours of flight time (excluding the origin)
    count = 0

    for city in distance:
        if city != origin and distance[city] <= k:
            count += 1


    return count


    

# 37 minutes


# Test Cases

connections1 = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), 
                ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

connections2 = []


origin = "New York"

k1 = 5
k2 = 7
k3 = 8
k4 = 0


print(VacationDestinations(connections1, origin, k1))
print(VacationDestinations(connections1, origin, k2))
print(VacationDestinations(connections1, origin, k3))

# My Added Test Cases
print(VacationDestinations(connections1, origin, k4))
print(VacationDestinations(connections2, origin, k3))