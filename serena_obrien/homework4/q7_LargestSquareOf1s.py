# Time complexity: O(n^2)
# Space complexity: O(n^2)
# I think it could be optimized to O(n)?

# Technique: Dynamic programming: tabulation

def LargestSquareOf1s(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0] * cols for _ in range(rows)]
    max_size = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )
                
                max_size = max(max_size, dp[i][j])

    return max_size

if __name__ == "__main__":
    inputs = [[[0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1]], [[]]]

    for input in inputs:
        for i in range(len(input)):
            for j in range(len(input[0])):
                print(input[i][j], end=" ")
            print()
        print()

        print(f"Dimension: {LargestSquareOf1s(input)}")

# ~ time spent: ~25 minutes