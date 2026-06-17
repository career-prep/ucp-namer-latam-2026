# Technique: Dynamic programming - tabulation
# time complexity: O(n^2)
# space complexity: O(n^2)

def largest_square_of_1s(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    biggest = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = 1 + min(dp[row - 1][col],
                                           dp[row][col - 1],
                                           dp[row - 1][col - 1])
                biggest = max(biggest, dp[row][col])
    return biggest

#test cases
matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
]
matrix2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0],
]

assert largest_square_of_1s(matrix1) == 2
assert largest_square_of_1s(matrix2) == 3
assert largest_square_of_1s([[0, 0], [0, 0]]) == 0
assert largest_square_of_1s([]) == 0

# edge cases
assert largest_square_of_1s([[1]]) == 1
assert largest_square_of_1s([[0]]) == 0
assert largest_square_of_1s([[1, 1], [1, 1]]) == 2
assert largest_square_of_1s([[1, 0, 1], [1, 1, 1], [1, 1, 1]]) == 2
assert largest_square_of_1s([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 1

print("yay!!")

# Time spent: ~20 minutes
