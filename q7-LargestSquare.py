def largestSquare(matrix):
    ROW, COL = len(matrix), len(matrix[0])
    dp = [[0] * COL for _ in range(ROW)]
    max_size = 0

    for i in range(ROW):
        for j in range(COL):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                max_size = max(max_size, dp[i][j])
    
    return max_size

matrix = [
    [0,1,0,1],
    [0,0,1,1],
    [0,1,1,1],
    [0,0,1,1]
]
print(largestSquare(matrix))