# Data Structure: Graph
# Algorithm: Generical traversal
# Time Complexity: O(R * C) since we visit every cell in the grid exactly once
# Space Complexity: O(R * C) since the recursion stack could go up to the total number of cells

def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    seen = set()
    island_count = 0

    def dfs(r, c):
        # Account for edge cases, already seen, or water
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in seen):
            return
        
        seen.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in seen:
                island_count += 1
                dfs(r, c)

    return island_count

test_grid_1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

test_grid_2 = [
    [1, 0, 0],
    [0, 0, 0]
]


print(num_islands(test_grid_1)) # Output: 3
print(num_islands(test_grid_2)) # Output: 1

# Time Spent: 23 min