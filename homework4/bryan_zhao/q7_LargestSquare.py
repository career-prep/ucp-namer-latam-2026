# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O (M X N) where M is # of rows and N is # of columns
# Space Complexity: O (M X N)

def largest_square(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                dp[r + 1][c + 1] = 1 + min(dp[r][c+1], dp[r + 1][c], dp[r][c])
                max_side = max(max_side, dp[r + 1][c + 1])
    
    return max_side

grid1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]

grid2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]

print(largest_square(grid1))
print(largest_square(grid2))

# Time Spent: 30 minutes