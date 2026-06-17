def numberOfIslands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    def dfs(r, c):
        if (min(r, c) < 0 or r == rows or c == cols):
            return
        if matrix[r][c] == 0:
            return
        
        matrix[r][c] = 0

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                count += 1
                dfs(r, c)

    return count

if __name__ == "__main__":

    matrix1 = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    print("Test 1 (expect 3):", numberOfIslands(matrix1))

    matrix2 = [
        [1, 0, 0],
        [0, 0, 0],
    ]
    print("Test 2 (expect 1):", numberOfIslands(matrix2))