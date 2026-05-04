# Runtime: O(V + E)
# Space complexity: O(V + E)
# Data Structure: Graph
# Algorithm: BFS
# Time Spent: 35 minutes

import collections
def alternatingPath(edges, origin, destination):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append((edge[1], edge[2]))

    visited = set()
    q = collections.deque()
    color = None
    q.append((origin, color))
    visited.add((origin, color))
    path = 0
    while q:
        for i in range(len(q)):
            curr, color = q.popleft()
            if curr == destination:
                return path
            for nei, edgeColor in graph[curr]:
                if (nei, edgeColor) not in visited and color != edgeColor:
                    q.append((nei, edgeColor))
                    visited.add((nei, edgeColor))
        path += 1
    return -1


edges1 = [("A", "B", "blue"), ("A","C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]
edges2 = [("A", "B", "blue"), ("B", "C", "red"), ("C", "D", "blue"), ("D", "A", "red")]

# Test Case with path
print(alternatingPath(edges1, "A", "E"))
# Test Case with no path
print(alternatingPath(edges1, "E", "D"))
# Test Case with path of 0
print(alternatingPath(edges2, "A", "A"))
# Test Case with path of 1
print(alternatingPath(edges2, "A", "B"))
# Test Case with no path with cycle
print(alternatingPath(edges2, "A", "Z"))
# Test Case with no path with no cycle
print(alternatingPath(edges1, "A", "Z"))
# Test Case with two paths from a node
edges3 = [("A", "B", "red"), ("A", "B", "blue"), ("B", "C", "blue")]
print(alternatingPath(edges3, "A", "C"))
