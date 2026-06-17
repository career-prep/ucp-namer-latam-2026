def numberOfIslands(matrix):
    """
    idea:
    go through each element in matrix
        if that element = 1 -> island -> number of islands += 1
            from there, use dfs to recursively find its adjacent positions
            to mark all its areas - mark 1 to 0 as visited

    Time complexity: O(mn) (m: number of rows, n: number of columns)
    Space complexity: O(mn)
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    islands = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 0:
            return

        matrix[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                islands += 1
                dfs(i, j)

    return islands


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(str(value) for value in row))


example1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

example2 = [
    [1, 0, 0],
    [0, 0, 0],
]

print("example 1 input:")
printMatrix(example1)
print(f"number of islands: {numberOfIslands([row[:] for row in example1])}")

print("example 2 input:")
printMatrix(example2)
print(f"number of islands: {numberOfIslands([row[:] for row in example2])}")
