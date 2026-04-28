# Question 4: NumberOfIslands

# Data Structure: Graph
# Algorithm: DFS (flood fill) — visit each cell once, sink visited land cells
# Time Complexity: O(m * n) where m and n are the matrix dimensions
# Space Complexity: O(m * n) for the visited set and DFS call stack


def numberOfIslands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if (r, c) in visited or matrix[r][c] == 0:
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count


# --- Tests ---

# Test 1: 3 islands
matrix1 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
]
print("Test 1:", numberOfIslands(matrix1))  # 3

# Test 2: 1 island (all land in a row)
matrix2 = [
    [1, 0, 0],
    [0, 0, 0],
]
print("Test 2:", numberOfIslands(matrix2))  # 1

# Test 3: no land
matrix3 = [
    [0, 0],
    [0, 0],
]
print("Test 3:", numberOfIslands(matrix3))  # 0

# Test 4: entire grid is one island
matrix4 = [
    [1, 1],
    [1, 1],
]
print("Test 4:", numberOfIslands(matrix4))  # 1

# Test 5: single cell
print("Test 5:", numberOfIslands([[1]]))  # 1
print("Test 6:", numberOfIslands([[0]]))  # 0

# Test 7: empty matrix
print("Test 7:", numberOfIslands([]))     # 0

# Spent a total of 25 mins on this question
