# Runtime:
# Time: O(n^2)
# Space: O(n^2)
# Implementation time: 40 minutes


def largest_square_of_ones(matrix):
    #1. Handle edge cases
    if not matrix or not matrix[0]:
        return 0

    #2. Declare variables
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    largest = 0

    #3. Iterate through matrix
    for row in range(rows):
        for col in range(cols):

            #4. Update square size
            if matrix[row][col] == 1:
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = 1 + min(
                        dp[row - 1][col],
                        dp[row][col - 1],
                        dp[row - 1][col - 1]
                    )

                largest = max(largest, dp[row][col])

    #5. Return largest dimension
    return largest


def Test_LargestSquareOfOnes():
    #1. Declare test cases
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

    #2. Run tests
    print("Input 1:")
    print(matrix1)
    print("Output:", largest_square_of_ones(matrix1))
    print()

    print("Input 2:")
    print(matrix2)
    print("Output:", largest_square_of_ones(matrix2))


if __name__ == "__main__":
    Test_LargestSquareOfOnes()