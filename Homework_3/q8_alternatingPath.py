# Question 8: AlternatingPath
#
# Given an origin and a destination in a directed graph in which edges can be blue or red,
# determine the length of the shortest path from the origin to the destination in which
# the edges traversed alternate in color. Return -1 if no such path exists.
#
# Examples:
#
# Input: [(A, B, "blue"), (A, C, "red"), (B, D, "blue"), (B, E, "blue"), (C, B, "red"),
#          (D, C, "blue"), (A, D, "red"), (D, E, "red"), (E, C, "red")]
#
# Input: origin = A, destination = E
# Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))
#
# Input: origin = E, destination = D
# Output: -1 (only path is: E→C (red), C→B (red), B→D (blue))
#          — invalid because red follows red (not alternating)



from collections import deque
def alternating_path(origin,destination,edges):
    graph={}
    for a,b,color in edges:
        if a not in graph:
            graph[a] = []
        graph[a].append((b,color))

    queue = deque([(origin, "blue", 0), (origin, "red", 0)])
    visited = set()

    while queue:
        node, last_color, steps = queue.popleft()

        if node == destination:
            return steps

        if (node, last_color) in visited:
            continue
        visited.add((node, last_color))

        if node not in graph:
            continue

        for nei, color in graph[node]:
            if color != last_color:
                queue.append((nei,color,steps + 1))

    return -1

edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"),
         ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"),
         ("E", "C", "red")]

print(alternating_path("A", "E", edges))    
print(alternating_path("E", "D", edges))    



#One of the toughest question solved. Had to seek help from AI 