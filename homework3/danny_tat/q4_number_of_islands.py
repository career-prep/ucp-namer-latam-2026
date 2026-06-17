from collections import deque

# Data Structure: Graph, Queue
# Algorithm: Breadth-First Search
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Given a binary matrix in which 1s represent land and 0s represent water, return the number of islands


def numberOfIslands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited[r][c] = True
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols \
                        and not visited[nr][nc] and matrix[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                count += 1

    return count


# Test Case
matrix1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
print(numberOfIslands(matrix1))
print(numberOfIslands([[1, 0, 0],
                       [0, 0, 0]]))

# time: 35 min
