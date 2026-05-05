# Method: DFS
# Space Complexity: O(M * N)
# Time Complexity: O(M * N)
# Total Time Taken: 40 mins

def NumberOfIslands(matrix):
    if not matrix:
        return 0
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == 0:
            return

        matrix[r][c] = 0

        dfs(r + 1, c) # Down
        dfs(r - 1, c) # Up
        dfs(r, c + 1) # Right
        dfs(r, c - 1) # Left

# Run through each item in the matrix, once hitting a 1, increase counter by 1 and 
# use dfs to change entire island to be 0 so it is not counted again. 
# Repeat until reaching the end of the matrix

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                count += 1
                dfs(r, c)
    return count

grid1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

grid2 = [
    [1, 0, 0],
    [0, 0, 0]
]

grid3 = []

print(NumberOfIslands(grid1))
print(NumberOfIslands(grid2))
print(NumberOfIslands(grid3))