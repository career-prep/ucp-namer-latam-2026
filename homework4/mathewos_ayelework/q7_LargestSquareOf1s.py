# technique: dynamic programming - tabulation
# time complexity: O(n^2) where n = matrix dimension
# space complexity: O(n^2)
# time taken: 30 mins

def largestSquareOf1s(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    # dp[r][c] = side length of largest square whose bottom-right corner is (r, c)
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                max_side = max(max_side, dp[r][c])

    return max_side


matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
print(largestSquareOf1s(matrix1))  # 2

matrix2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]
print(largestSquareOf1s(matrix2))  # 3

print(largestSquareOf1s([[1]]))    # 1
print(largestSquareOf1s([[0]]))    # 0
