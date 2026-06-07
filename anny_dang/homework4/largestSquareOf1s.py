def largestSquareOf1s(square):
    """
    idea:
    - create dp with same matrix as square and set all to 0
    - largest = 0 
    - walk through each cell forward 
        - if value at that cell = 1
            - if position of that cell = 0 -> dp[cell] = 1
            - else:
                -> dp[cell] = 1 + min(dp[top cell], dp[left cell], dp[top left cell])
            - update largest if dp[cell] > largest
    - return largest

    time: O(n^2)
    space: O(n^2)
    """
    n = len(square)
    dp = [[0]*n for _ in range(n)]
    largest = 0

    for r in range(n):
        for c in range(n):
            if square[r][c] == 1:
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                largest = max(largest, dp[r][c])
    
    return largest


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

print("Input 1 ->", largestSquareOf1s(matrix1))
print("Input 2 ->", largestSquareOf1s(matrix2))
