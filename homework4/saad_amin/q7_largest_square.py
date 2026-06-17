# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(rows * cols)
# Space Complexity: O(rows * cols)


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
                    dp[r][c] = 1 + min(
                        dp[r - 1][c],
                        dp[r][c - 1],
                        dp[r - 1][c - 1]
                    )

                largest = max(largest, dp[r][c])

    return largest


def main():
    matrix1 = [
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]
    ]

    matrix2 = [
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0]
    ]

    print(largest_square(matrix1))  # 2
    print(largest_square(matrix2))  # 3


if __name__ == "__main__":
    main()
    
#Time: 35 min