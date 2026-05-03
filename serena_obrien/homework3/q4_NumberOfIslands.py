# Time complexity: O(m x n)
# Space complexity: O(m x n)

# Technique: Generic traversal

from collections import deque

def NumberOfIslands(grid):
    if not grid:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    
    numIslands = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                numIslands += 1
                q.append((i, j))
                grid[i][j] = "-" # marking visited

                while q:
                    curr = q.popleft()
                    i, j = curr
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                            grid[ni][nj] = "-"
                            q.append((ni, nj))
    return numIslands

if __name__ == "__main__":
    grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]

    grid2 = [
    ["1","0","1","1","1"],
    ["1","1","0","1","1"],
    ["0","1","0","0","0"],
    ["0","0","0","1","0"],
    ["0","0","0","0","0"]
    ]

    grid3 = [
    ["1","0","0"],
    ["0","0","0"]
    ]

    grids = (grid1, grid2, grid3)

    for grid in grids:
        print(NumberOfIslands(grid))

# ~ time spent: 30 minutes