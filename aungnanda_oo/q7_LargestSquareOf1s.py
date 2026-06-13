# Question 7: LargestSquareOf1s

# Technique: Dynamic programming (tabulation)
# dp[i][j] = side length of the largest square of 1s whose bottom-right
# corner is at (i, j).
# If matrix[i][j] == '1': dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# If matrix[i][j] == '0': dp[i][j] = 0
# Answer: max over all dp[i][j].

# Assumption: matrix is given as a flat list read left-to-right, top-to-bottom,
# and n is the number of rows/cols (square matrix).

# Time Complexity:  O(n^2)
# Space Complexity: O(n^2) for the dp table (reducible to O(n) with rolling row)


def largestSquareOf1s(matrix, n):
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    best = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                best = max(best, dp[i][j])
    return best
# Time Complexity = O(n^2), Space Complexity = O(n^2)


# --- Tests ---

# Example 1 (4x4): expected output 2
m1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
]
print("Example 1:", largestSquareOf1s(m1, 4))  # 2

# Example 2 (5x5): expected output 3
m2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0],
]
print("Example 2:", largestSquareOf1s(m2, 5))  # 3

# All zeros
m3 = [[0, 0], [0, 0]]
print("All zeros:", largestSquareOf1s(m3, 2))  # 0

# All ones 3x3
m4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print("All ones 3x3:", largestSquareOf1s(m4, 3))  # 3

# Spent a total of 25 mins on this question
