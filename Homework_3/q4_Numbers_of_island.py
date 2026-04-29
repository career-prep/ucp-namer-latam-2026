# Given a binary matrix where 1s represent land and 0s represent water,
# return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).
#
# Example 1:
# Input:
# [[1, 0, 1, 1, 1],
#  [1, 1, 0, 1, 0],
#  [1, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0]]
# Output: 3
#
# Example 2:
# Input:
# [[1, 0, 0],
#  [0, 0, 0]]
# Output: 1


def num_island(grid):
    m,n=len(grid),len(grid[0])
    def dfs(row,col):
        if row<0 or row>=m or col<0 or col>=n or grid[row][col]!='1':
            return 
        else:
            grid[row][col]='0'
            dfs(row,col+1)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row-1,col)
    count=0
    for row in range(m):
        for col in range(n):
            if grid[row][col]=='1':
                count+=1
                dfs(row,col)
    return count

grid1 = [
    ["1", "1", "1"],
    ["1", "1", "0"],
    ["1", "0", "1"]
]
print(num_island(grid1))

grid2 = [
    ["1", "0", "1"],
    ["0", "1", "0"],
    ["1", "0", "1"]
]
print(num_island(grid2))

grid3 = [
    ["0", "0"],
    ["0", "0"]
]
print(num_island(grid3))

grid4 = [
    ["1", "1"],
    ["1", "1"]
]
print(num_island(grid4)) 


#Time Complexity: O(mxn)
#Space Complexity: O(mxn)

#Spent 30 mins