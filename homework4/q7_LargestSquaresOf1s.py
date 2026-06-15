# Runtime: O(n^2)
# Space complexity: O(n)
# Technique: DP Tabulization
def largestSquare(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    maxD = 0
    prev = None
    dp = None
    for i in range(rows):
        prev = dp
        dp = [0] * cols
        for j in range(cols):
            if not prev or j == 0:
                dp[j] = matrix[i][j]
            elif matrix[i][j] == 1 and matrix[i-1][j-1] == 1 and matrix[i-1][j] == 1 and matrix[i][j-1] == 1:
                dp[j] = prev[j-1] + 1
            elif matrix[i][j] == 1:
                dp[j] = 1
            maxD = max(maxD, dp[j])
    return maxD

grid1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
grid2 = [
    [0,1,0,1,1],
    [0,0,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [0,1,1,0,0]
]
grid3 = [[]]
grid4 = [[1]]
grid5 = [
    [1,1,1,1,1,1]
]
grid6 = [
    [1,1,1,1],
    [1,0,1,1],
    [1,1,1,1],
    [1,1,1,1]
]
print(largestSquare(grid1) == 2)
print(largestSquare(grid2) == 3)
print(largestSquare(grid3) == 0)
print(largestSquare(grid4) == 1)
print(largestSquare(grid5) == 1)
print(largestSquare(grid6) == 2)

# Time Spent: 35:00
