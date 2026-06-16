# Technique: Dynamic programming (tabulation)
# dp[i][j] = side of largest all-1s square ending at (i, j)
# Time: O(rows * cols)
# Space: O(rows * cols)


def largestSquareOf1s(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    best = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                best = max(best, dp[i][j])
    return best


print(largestSquareOf1s([[0, 1, 0, 1],
                         [0, 0, 1, 1],
                         [0, 1, 1, 1],
                         [0, 0, 1, 1]]))  # 2

print(largestSquareOf1s([[0, 1, 0, 1, 1],
                         [0, 0, 1, 1, 1],
                         [1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1],
                         [0, 1, 1, 0, 0]]))  # 3

# Time spent: ~30 minutes