# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(n * m) where n is number of rows and m is number of columns
# Space Complexity: O(n * m) where n is number of rows and m is number of columns

def largest_square(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    largest = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = (min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1)

                largest = max(largest, dp[r][c])
    return largest

# Time Taken: 22mins 31secs

# Testcases:
matrix_1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
print(largest_square(matrix_1))

matrix_2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]
print(largest_square(matrix_2))

# Edge Cases:
matrix_3 = [ # All zeros
    [0, 0],
    [0, 0]
]
print(largest_square(matrix_3))

matrix_4 = [ # All ones
    [1, 1],
    [1, 1]
]
print(largest_square(matrix_4))
