# Data Structure: Graph + DFS
# Technique: DFS flood-fill to sink visited land cells
# Time Complexity: O(m * n) where m = rows, n = cols
# Space Complexity: O(m * n) worst case recursion stack

def numberOfIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        # out of bounds or water -> stop
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return
        grid[r][c] = 0  # marking as visited by sinking the land
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                dfs(r, c)   # sink the whole island

    return count


# Test 1: example from assignment -> 3 islands
grid1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
]
print(numberOfIslands(grid1))   # 3

# Test 2: example from assignment -> 1 island
grid2 = [
    [1, 0, 0],
    [0, 0, 0],
]
print(numberOfIslands(grid2))   # 1

# Test 3: all water -> 0
grid3 = [
    [0, 0, 0],
    [0, 0, 0],
]
print(numberOfIslands(grid3))   # 0

# Test 4: all land -> 1 big island
grid4 = [
    [1, 1],
    [1, 1],
]
print(numberOfIslands(grid4))   # 1

# Test 5: each cell its own island
grid5 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
]
print(numberOfIslands(grid5))   # 5

# Time spent: ~30 minutes