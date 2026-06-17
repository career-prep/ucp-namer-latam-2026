# Data structure: Graph - DFS
# Time: O(m * n)
# Space: O(m * n) worst case


def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])

    def explore_island(r, c):
        stack = [(r, c)]
        while stack:
            i, j = stack.pop()
            if i < 0 or i >= rows or j < 0 or j >= cols:
                continue
            if grid[i][j] != 1:
                continue
            grid[i][j] = 0
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
                explore_island(i, j)
    return count


grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
print("Correct:", 1)
print("Output: ", num_islands([r[:] for r in grid]))
print()

grid = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1],
]
print("Correct:", 3)
print("Output: ", num_islands([r[:] for r in grid]))
print()

grid = [[0, 0], [0, 0]]
print("Correct:", 0)
print("Output: ", num_islands([r[:] for r in grid]))
print()

grid = [[1]]
print("Correct:", 1)
print("Output: ", num_islands([r[:] for r in grid]))
print()

print("Correct:", 0)
print("Output: ", num_islands([]))
print()

# time taken: 24 min
