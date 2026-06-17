def largest_square_of_1s(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side

    
if __name__ == "__main__":
    matrix1 = [
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]
    ]
    print(largest_square_of_1s(matrix1))  # 2

    matrix2 = [
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0]
    ]
    print(largest_square_of_1s(matrix2))  # 3

    print(largest_square_of_1s([[1]]))    # 1
    print(largest_square_of_1s([[0]]))    # 0

    # Time spent: 40 minutes