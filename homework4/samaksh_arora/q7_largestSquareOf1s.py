#Samaksh Arora
#Question 7 - Largest Square of 1s
#Dynamic programming (Tabulation)
#Time Complexity: O(m * n) where m and n are the dimensions of the matrix
#Space Complexity: O(m * n) for the DP table
#Time Spent: >40 minutes


def largestSquareOf1s(matrix):
    
    numberOfRows = len(matrix)
    numberOfColumns = len(matrix[0])
    dp = [[0] * numberOfColumns for _ in range(numberOfRows)]
    maxSquareSide = 0
    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                maxSquareSide = max(maxSquareSide, dp[i][j])
    return maxSquareSide

#Test Cases
matrix1 = [[0,1,0,1],[0,0,1,1],[0,1,1,1],[0,0,1,1]]
assert largestSquareOf1s(matrix1) == 2
matrix2 = [[0,1,0,1,1],[0,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,0,0]]
assert largestSquareOf1s(matrix2) == 3

# Extra: 
assert largestSquareOf1s([[1,1],[1,1]]) == 2
assert largestSquareOf1s([[0]]) == 0
