#dynamic programming
#time complexity: O(n^2)
#space complexity: O(n^2)

def LargestSquareOf1s(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    table = [[0]* cols for _ in range(rows)]
    maxsquare = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                table[i][j] = 0
            elif i==0 or j == 0:
                table[i][j] = matrix[i][j]
            else:
                table[i][j] = min(table[i-1][j], table[i-1][j-1], table[i][j-1]) + 1

            if table[i][j] > maxsquare:
                maxsquare = table[i][j]
            
    return maxsquare

#test cases
matrix = [[1, 0, 1, 1],[1, 1, 1, 1],[1, 1, 1, 0],[0, 1, 1, 1]]
print(LargestSquareOf1s(matrix))

