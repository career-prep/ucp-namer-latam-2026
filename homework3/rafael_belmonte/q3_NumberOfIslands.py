# Data Structure: Graph (implicit grid graph)
# Algorithm: Generic traversal (DFS used here; BFS would be equivalent in Big-O).
#
# Each cell is a node; edges connect orthogonally adjacent land cells.
# Walk every unvisited land cell, flood-fill it, and increment the island count.
#
# Time complexity:  O(R * C) — every cell visited at most once.
# Space complexity: O(R * C) for the visited set / recursion stack in the worst case.


def number_of_islands(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def dfs(r, c):
        # iterative to avoid Python recursion limits on large grids
        stack = [(r, c)]
        while stack:
            i, j = stack.pop()
            if i < 0 or i >= rows or j < 0 or j >= cols:
                continue
            if visited[i][j] or grid[i][j] != 1:
                continue
            visited[i][j] = True
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                dfs(r, c)
    return count


# test cases
if __name__ == "__main__":
    grid1 = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    assert number_of_islands(grid1) == 3

    grid2 = [
        [1, 0, 0],
        [0, 0, 0],
    ]
    assert number_of_islands(grid2) == 1

    assert number_of_islands([]) == 0
    assert number_of_islands([[0, 0], [0, 0]]) == 0
    assert number_of_islands([[1, 1, 1], [1, 1, 1]]) == 1

    print("yay!!")

# Time spent: ~20 minutes
