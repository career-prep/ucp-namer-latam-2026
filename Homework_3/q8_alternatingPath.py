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



from collections import defaultdict, deque

def alternating_path(edges, origin, destination):
    graph=defaultdict(list)
    for u,v,color in edges:
        graph[u].append((v,color))
    queue=deque([(origin,None,0)])
    visited=set([(origin,None)])
    while queue:
        node,last_color,dist=queue.popleft()
        if node==destination:
            return dist
        for nei, color in graph[node]:
            if color!=last_color and (nei,color) not in visited:
                visited.add((nei,color))
                queue.append((nei,color,dist+1))
    return -1

edges=[("A","B","blue"),
       ("A","C","red"),
       ("B","D","blue"),
       ("B","E","blue"),
       ("C","B","red"),
       ("D","C","blue"),
       ("A","D","red"),
       ("D","E","red"),
       ("E","C","red")
]

print(alternating_path(edges,"A","E"))
print(alternating_path(edges,"E","D"))
print(alternating_path(edges,"A","A"))

edges2=[("A","B","blue"),("B","C","blue")]
print(alternating_path(edges2,"A","C"))

edges3=[("A","B","red")]
print(alternating_path(edges3,"A","B"))  



#One of the toughest question solved. Had to seek help from AI 

#Time Complexity: O(V+E)
#Space Complexity: O(V+E)

#Spent 50 mins