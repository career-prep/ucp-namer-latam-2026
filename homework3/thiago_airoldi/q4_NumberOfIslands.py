# Graph Generic Traversal, either BFS or DFS works just as effectively, but I chose to use DFS since it seemed more intuitive.
# O(m * n) Time Complexity, where m is the number of rows and n is the number of columns. (In worst case, we loop through each position in the grid)
# O(m * n) Space Complexity, where m is the number of rows and n is the number of columns. (In worst case, recursive call stack holds all positions of the grid)
# Given a binary matrix in which 1's represent land and 0's represent water, return the number of islands. 


def numberOfIslands(grid):

    if not grid:
        return None # I feel like returning 0 could be confusing because there can be valid inputs that actually have zero islands. Returning None
                    # is better to signify that something is wrong. (Although, I would ask an interviewer before assuming)
    
    # Store dimensions of the grid.
    ROWS = len(grid)
    COLS = len(grid[0])

    # Store the number of islands we find.
    islandCount = 0


    # This function turns every current and adjacent 1 into a 0 so that while looping over the grid, we do not recount islands we have already counted.
    # By doing this, we can avoid using extra memory by storing positions we have already visited in a set.
    def dfs(row, col):

        # If current position is out of bounds, exit.
        if row < 0 or col < 0 or row >= ROWS or col >= COLS:
            return
        
        # If current position is marked as water, exit.
        if grid[row][col] == 0:
            return
        

        # If we get here, our current position is a '1', that must be marked as '0' so we do not visit or count it again.
        grid[row][col] = 0


        # Now traverse up, left, right, and down, to mark all adjacent 1's as 0's.

        # Up
        dfs(row-1, col)

        # Left
        dfs(row, col-1)

        # Right
        dfs(row, col+1)

        # Down
        dfs(row+1, col)



    # Loop through each position in the grid. Once we encounter a '1', run a dfs to mark all adjacent 1's as 0's, and then increase islandCount.
    for r in range(ROWS):
        for c in range(COLS):

            if grid[r][c] == 1:
                dfs(r, c)
                islandCount += 1


    return islandCount




# 17 minutes



# Test Cases
grid1 = [[1, 0, 1, 1, 1], 
         [1, 1, 0, 1, 1], 
         [0, 1, 0, 0, 0], 
         [0, 0, 0, 1, 0], 
         [0, 0, 0, 0, 0]]


grid2 = [[1, 0, 0],
         [0, 0, 0]]

grid3 = []



print(numberOfIslands(grid1))
print(numberOfIslands(grid2))

# My Added Test Cases
print(numberOfIslands(grid3))

