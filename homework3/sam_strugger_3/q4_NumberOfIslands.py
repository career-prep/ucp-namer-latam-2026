# O(m * n) time and space complexity because of the recursive call stack. 
# This is a generic traversal problem. I used DFS to solve it. The data structure is a 2d array or matrix.  
def numberOfIslands(grid):
    # Plan 
    # When we find a 1 call DFS on it. 
    # Recursively change the value of each adjacent
    # Tile and add one to island count 
    
    count = 0
    ROWS = len(grid)
    COLUMNS = len(grid[0])

    def dfs(i,j):
        offsets = [(0,1),(0,-1),(1,0),(-1,0)]
        grid[i][j]+=count+1
            
        for ro, co in offsets:
            if 0 <= i+ro < ROWS and 0 <= j+co < COLUMNS:
                neighbor = grid[i+ro][j+co]

                if neighbor == 1:
                    dfs(i+ro,j+co)

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == 1:
                count+=1
                dfs(row,column)

    return count


grid1 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
test1 = numberOfIslands(grid1)
print(test1)

grid2 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
test2 = numberOfIslands(grid2)
print(test2)

# I spent 20 minutes on this
