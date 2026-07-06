# Method: DP
# Space Complexity: O(R * C)
# Time Complexity: O(R * C)
# Total Time Taken: 40 mins
# Use DP to mark the largest square possible at each position. 
# Using that you can look at the values already computed for the three neighbors(Top, Left, and Top-Left). 
# If any of those has a 0, then the current square is the largest possible at that position.


def LargestSquareOf1s(matrix):
    if not matrix or not matrix[0]:
        return 0

    row = len(matrix)
    col = len(matrix[0])
    
    DP = [[0] * col for _ in range(row)]
    max_side = 0

    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    DP[r][c] = 1
                else:
                    DP[r][c] = min(DP[r-1][c], DP[r][c-1], DP[r-1][c-1]) + 1
                
                max_side = max(max_side, DP[r][c])
            else:
                DP[r][c] = 0

    return max_side

matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
print(LargestSquareOf1s(matrix1))

matrix2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]
print(LargestSquareOf1s(matrix2))

matrix3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(LargestSquareOf1s(matrix3))