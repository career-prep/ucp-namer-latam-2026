# Dynamic Programming - Tabulation
# O(n^2) Time Complexity, where n is the number of rows and columns since the given matrix is square
# O(n^2) Space Complexity, because of the dp matrix
# Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.

def largestSquareOfOnes(matrix):

    # If there is no matrix given, then there is no largest square
    if not matrix or not matrix[0]:
        return 0
    

    # At first I thought this problem might be solved using a queue in a BFS traversal type of way, but I could not figure out
    # how to make that work...

    # My next guess is that this problem could be solved using dynamic programming. If we could somehow figure out the dimension of
    # the current cell based on the dimensions of the adjacent cells then we could probably solve this problem.

    # My intuition is to make a dp matrix in which dp[r][c] holds the dimension of a square at (r, c) in which (r, c) one of the 
    # corners of the square. The most useful corner would probably be the bottom right corner because when you look at larger
    # cases where the largest square is at least 3x3, you can more easily see that the left, up, and up-left diagonal cells are
    # right corners of their own squares which are exactly one dimension smaller.

    # For example, if dp[r][c - 1] = 1, and dp[r - 1][c] = 1, and dp[r - 1][c - 1] = 1, then we could conclude that dp[r][c] = 2
    # (as long as matrix[r][c] is a 1 instead of a zero)
    
    # I will initialize my dp matrix with zeros at first since any cell of 0 in the input matrix should remain zero in the dp matrix
    ROWS = len(matrix)
    COLS = len(matrix[0])

    dp = [[0] * COLS for _ in range(ROWS)]


    # Checks if a position (r, c) is inbounds in the matrix
    def inBounds(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            return False
        else:
            return True
        

    # Stores the largest dimension
    res = 0

    for r in range(ROWS):
        for c in range(COLS):

            # Skip zeros
            if matrix[r][c] == 0:
                continue

            # Now we are on a 1, so at the bare minimum, this position in the dp matrix will hold 1
            dp[r][c] = 1

            # Make sure we can access the required neighbors (left, up, up-left diagonal)
            if inBounds(r, c - 1) and inBounds(r - 1, c) and inBounds(r - 1, c - 1):

                # In the happy case where all important neighboring cells have the same value, then min() returns that "same" value
                # and we just add 1 to that value to get the correct result in dp[r][c]

                # However, in the case where the neighbors have different values because each cell might be part of differently
                # sized squares (or they may be 0's in matrix), we can only add this cell to the smallest value
                dp[r][c] = 1 + min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1])


            res = max(res, dp[r][c])


    return res



# 37 minutes

# Test Cases

matrix1 = [[0, 1, 0, 1],
           [0, 0, 1, 1],
           [0, 1, 1, 1],
           [0, 0, 1, 1]]


matrix2 = [[0, 1, 0, 1, 1],
           [0, 0, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [0, 1, 1, 0, 0]]



print(largestSquareOfOnes(matrix1))
print(largestSquareOfOnes(matrix2))