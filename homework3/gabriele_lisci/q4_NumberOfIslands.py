# Runtime: O(n*m)
# Space complexity: O(n*m)
# Data Structure: Graph
# Algorithm: BFS

import collections
def numberOfIslands(graph):
    if not graph:
        return 0
    def bfs(source, graph, visited):
        n = len(graph)
        m = len(graph[0])
        q = collections.deque()
        q.append(source)
        visited.add(source)
        while q:
            curr = q.popleft()
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            for d in dirs:
                newDir = (curr[0] + d[0], curr[1] + d[1])
                if 0 <= newDir[0] < n and 0 <= newDir[1] < m and newDir not in visited and graph[newDir[0]][newDir[1]] == 1:
                    q.append(newDir)
                    visited.add(newDir)

    islands = 0
    visited = set()
    n = len(graph)
    m = len(graph[0])
    for i in range(n):
        for j in range(m):
            if ((i,j) not in visited and graph[i][j] == 1):
                islands += 1
                bfs((i,j), graph, visited)
    return islands

testCase1 = [[1,0,1,1,1],[1,1,0,1,1],[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,0]]
testCase2 = [[1,0,0],[0,0,0]]
testCase3 = None
testCase4 = [[0,0,0,0,0], [0,0,0,0,0]]
testCase5 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(numberOfIslands(testCase1))
print(numberOfIslands(testCase2))
print(numberOfIslands(testCase3))
print(numberOfIslands(testCase4))
print(numberOfIslands(testCase5))

# Time Spent: 30:00
