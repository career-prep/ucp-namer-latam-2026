# Number of Islands
# Data Structure: Graph
# Algorithm: DFS (generic traversal)
# Time Complexity: O(N * M) where N is the number of rows and M is the number of columns in the matrix
# Space Complexity: O(N * M) where N is the number of rows and M is the number of columns

def NumberOfIslands(matrix):

    def dfsMarkEntireIsland(currentRow, currentCol):
        if currentRow < 0 or currentRow >= numberOfRows:
            return 
        if currentCol < 0 or currentCol >= numberOfCols:
            return
        if (currentRow,currentCol) in setOfVisitedCells:
            return
        if matrix[currentRow][currentCol] == 0:
            return
        
        setOfVisitedCells.add((currentRow, currentCol))

        dfsMarkEntireIsland(currentRow - 1, currentCol)
        dfsMarkEntireIsland(currentRow + 1, currentCol)
        dfsMarkEntireIsland(currentRow, currentCol - 1)
        dfsMarkEntireIsland(currentRow, currentCol + 1)


    if not matrix:
        return 0
    
    numberOfRows = len(matrix)
    numberOfCols = len(matrix[0])
    
    setOfVisitedCells = set()

    islandCount = 0

    for currentRow in range(numberOfRows):
        for currentCol in range(numberOfCols):
            if matrix[currentRow][currentCol] == 1 and (currentRow, currentCol) not in setOfVisitedCells:
                islandCount += 1
                dfsMarkEntireIsland(currentRow,currentCol)

    
    return islandCount


#Test Cases

matrix1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
print(NumberOfIslands(matrix1))  # expected: 3

matrix2 = [
    [1, 0, 0],
    [0, 0, 0]
]
print(NumberOfIslands(matrix2))  # expected: 1

matrix3 = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
]

print(NumberOfIslands(matrix3)) #expected: 1

