# Algorithm: DFS flood-fill on a 4-connected grid
# Time Complexity: O(R * C)
# Space Complexity: O(R * C) for the visited matrix and recursion stack


def numberOfIslands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or grid[r][c] == 0:
            return
        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                dfs(r, c)
    return count


print("NumberOfIslands Results:")

grid1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
]
print(numberOfIslands(grid1))

grid2 = [
    [1, 0, 0],
    [0, 0, 0],
]
print(numberOfIslands(grid2))

grid3 = [
    [0, 0, 0],
    [0, 0, 0],
]
print(numberOfIslands(grid3))

grid4 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]
print(numberOfIslands(grid4))

grid5 = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
]
print(numberOfIslands(grid5))

print(numberOfIslands([]))
print(numberOfIslands([[]]))
