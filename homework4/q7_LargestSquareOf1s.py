# Array/String Technique: Dynamic programming - Tabulation
# Time Complexity: O(R * C) 
# Space Complexity: O(C)

def maximalSquare(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * (cols + 1)
    max_side = prev = 0
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            temp = dp[j]
            if matrix[i-1][j-1] == '1' or matrix[i-1][j-1] == 1:
                dp[j] = min(dp[j], dp[j-1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return max_side * max_side

if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print("Maximal square area:", maximalSquare(matrix))

# Time Spent: 30 minutes