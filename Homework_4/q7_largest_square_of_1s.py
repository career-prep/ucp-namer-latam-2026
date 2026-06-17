# Question 7: LargestSquareOf1s
# Given a square matrix of 0s and 1s, find the dimension of the largest square
# consisting only of 1s.

def largest_square_of_1s(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    largest = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = 1 + min(
                        dp[row - 1][col],
                        dp[row][col - 1],
                        dp[row - 1][col - 1],
                    )
                largest = max(largest, dp[row][col])
    return largest
matrix_one = [
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
]
matrix_two = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
]


print(largest_square_of_1s(matrix_one))
print(largest_square_of_1s(matrix_two))
print(largest_square_of_1s([[0, 0], [0, 0]]))
print(largest_square_of_1s([[1]]))


# Spent 25 mins
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
