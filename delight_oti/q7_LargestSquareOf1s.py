# Technique: Dynamic programming - Tabulation

def LargestSquare(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    dp = []

    for row in range(rows):
        dp.append([0] * cols)

    largest = 0

    for row in range(rows):

        for col in range(cols):

            if matrix[row][col] == 1:

                if row == 0 or col == 0:
                    dp[row][col] = 1

                else:
                    top = dp[row - 1][col]
                    left = dp[row][col - 1]
                    diagonal = dp[row - 1][col - 1]

                    dp[row][col] = 1 + min(top, left, diagonal)

                largest = max(largest, dp[row][col])

    return largest


# matrix1 = [
#     [0, 1, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 1, 1],
#     [0, 0, 1, 1]
# ]

# print(LargestSquare(matrix1))
# Output: 2


# matrix2 = [
#     [0, 1, 0, 1, 1],
#     [0, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [0, 1, 1, 0, 0]
# ]

# print(LargestSquare(matrix2))
# Output: 3