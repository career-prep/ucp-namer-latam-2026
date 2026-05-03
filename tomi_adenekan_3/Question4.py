time = n^2
space = 1
def island(mat):

    count = 0

    n = len(mat)
    m = len(mat[0])

    def dfs(mat, i, j):
        if j >= m  or i >= n or j < 0 or i < 0:
            return
        if mat[i][j] == 0:
            return
        mat[i][j] = 0
        dfs(mat, i+1, j )
        dfs(mat, i-1, j)
        dfs(mat, i, j+1)
        dfs(mat, i, j-1)

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                dfs(mat, i,j)
                count += 1

    return count
