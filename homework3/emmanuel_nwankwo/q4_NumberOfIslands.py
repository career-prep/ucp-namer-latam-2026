# Data Structure: Graph
# Algorithm: Breadth-first search
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

from collections import deque

def number_of_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    seen = set()
    islands = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        seen.add((r, c))
        directions = [[0,-1], [0,1], [1, 0], [-1, 0]]

        while queue:
            cell_row, cell_col = queue.popleft()
            for dr, dc in directions:
                next_cell_row, next_cell_col = cell_row + dr, cell_col + dc
                if (rows > next_cell_row >= 0 and cols > next_cell_col >= 0
                        and grid[next_cell_row][next_cell_col] == "1" and (next_cell_row, next_cell_col) not in seen):
                    queue.append((next_cell_row, next_cell_col))
                    seen.add((next_cell_row, next_cell_col))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in seen:
                bfs(row, col)
                islands += 1

    return islands

#Time Taken: 9mins 24secs

# Test cases:
grid = [["1", "0", "1", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "0"],
        ["0", "0", "0", "0", "0"]]

grid_1 = [["1", "0", "0"],
          ["0", "0", "0"]]

print(number_of_islands(grid))
print(number_of_islands(grid_1))

#Edge cases:
grid_2 = [["1"]]
grid_3 = [["0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]]

print(number_of_islands(grid_2))
print(number_of_islands(grid_3))