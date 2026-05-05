# Technique: Graph Traversal (DFS) on a 2D Grid

def numIslands(grid): # Time Complexity: O(R * C), Space Complexity: O(R * C)
    # 1. Handle edge case for empty input
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0

    # 2. Define a Depth-First Search (DFS) to explore contiguous land
    def dfs(r, c):
        # 3. Check boundaries and verify if cell is unvisited land (1)
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] == 0 or 
            (r, c) in visited):
            return
        
        # 4. Mark current coordinate as visited
        visited.add((r, c))
        
        # 5. Explore all 4 cardinal directions (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # 6. Iterate through every coordinate in the grid
    for r in range(rows):
        for c in range(cols):
            # 7. Start a new DFS traversal only when encountering unvisited land
            if grid[r][c] == 1 and (r, c) not in visited:
                island_count += 1
                dfs(r, c)

    return island_count

# Time Complexity: O(M * N) - each cell is visited at most once.
# Space Complexity: O(M * N) - for the visited set and recursion stack in the worst case.
# Time spent: 35 minutes

class Test:
    def run_tests(self):
        # 1. Test Case: Multiple islands
        grid1 = [
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        assert numIslands(grid1) == 3
        
        # 2. Test Case: Single island
        grid2 = [
            [1, 0, 0],
            [0, 0, 0]
        ]
        assert numIslands(grid2) == 1
        
        # 3. Test Case: All water
        grid3 = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        assert numIslands(grid3) == 0
        
        # 4. Test Case: All land
        grid4 = [
            [1, 1],
            [1, 1]
        ]
        assert numIslands(grid4) == 1
        
        print("NumIslands tests passed")

if __name__ == "__main__":
    Test().run_tests()