# Data Structure: Graph
# Algorithm: Depth-first search
# Time Complexity: O(M * N)
# Space Complexity: O(M * N)

def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return
        
        grid[r][c] = 0
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                islands += 1
                dfs(r, c)
                
    return islands

def main():
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    print(f"Test Case 1 - Result: {numIslands(grid1)}")

    grid2 = [[0, 0], [0, 0]]
    print(f"Test Case 2 - Result: {numIslands(grid2)}")

    grid3 = [[1, 1], [1, 1]]
    print(f"Test Case 3 - Result: {numIslands(grid3)}")

if __name__ == "__main__":
    main()

# Time Spent: 30 minutes