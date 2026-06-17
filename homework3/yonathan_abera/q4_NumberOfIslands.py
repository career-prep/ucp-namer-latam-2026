# Data Structure: Graph
# Algorithm: DFS
# Time Complexity: O(M * N)
# Space Complexity: O(M * N)

def numberOfIslands(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if matrix[r][c] == 0 or (r, c) in visited:
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count

matrix1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
]
print(numberOfIslands(matrix1)) 

matrix2 = [
    [1, 0, 0],
    [0, 0, 0],
]
print(numberOfIslands(matrix2)) 
print(numberOfIslands([[0, 0], [0, 0]])) 
print(numberOfIslands([[1, 1], [1, 1]]))

#Time spent: 37 minutes
