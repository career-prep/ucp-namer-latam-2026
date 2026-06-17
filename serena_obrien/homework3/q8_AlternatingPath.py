# Time complexity: O(V + E)
# Space complexity: O(V + E)

# Technique: Breadth-first traversal
from collections import deque

def AlternatingPath(edges, origin, destination):
    adjacencyList = {}
    for o, d, c in edges:
        if o not in adjacencyList: adjacencyList[o] = set()
        adjacencyList[o].add((d, c))

    visited = set()
    q = deque([(origin, None, 0)])
    visited.add((origin, None))

    while q:
        curr, currColor, distance = q.popleft()

        if curr == destination:
            return distance
        
        for neighbor, nColor in adjacencyList.get(curr, []):
            if currColor != nColor and (neighbor, nColor) not in visited:
                visited.add((neighbor, nColor))
                q.append((neighbor, nColor, distance + 1))

    return -1

if __name__ == "__main__":
    edges = ([("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")])

    # input = (origin, destination)
    inputs = (("A", "E"),
              ("E", "D"))

    for origin, destination in inputs:
        print(f"Length of shortest path from {origin} to {destination}: {AlternatingPath(edges, origin, destination)}")


# ~ time spent: 30 minutes