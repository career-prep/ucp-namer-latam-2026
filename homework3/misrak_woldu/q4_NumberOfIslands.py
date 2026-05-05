# Data Structure: Matrix / Grid
# Algorithm: Depth-First Search (DFS)
# Time Complexity: O(rows * cols)
# Space Complexity: O(rows * cols)

def count_islands(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    row_count = len(grid)
    col_count = len(grid[0])
    visited_cells = set()
    island_count = 0

    def dfs(row_index: int, col_index: int) -> None:
        if (
            row_index < 0
            or row_index >= row_count
            or col_index < 0
            or col_index >= col_count
            or grid[row_index][col_index] == 0
            or (row_index, col_index) in visited_cells
        ):
            return

        visited_cells.add((row_index, col_index))

        dfs(row_index + 1, col_index)  # down
        dfs(row_index - 1, col_index)  # up
        dfs(row_index, col_index + 1)  # right
        dfs(row_index, col_index - 1)  # left

    for row_index in range(row_count):
        for col_index in range(col_count):
            if grid[row_index][col_index] == 1 and (row_index, col_index) not in visited_cells:
                island_count += 1
                dfs(row_index, col_index)

    return island_count


def run_tests() -> None:
    assert count_islands([
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]) == 1

    assert count_islands([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]) == 3

    assert count_islands([]) == 0
    assert count_islands([[]]) == 0
    assert count_islands([[0, 0], [0, 0]]) == 0
    assert count_islands([[1, 1], [1, 1]]) == 1
    assert count_islands([[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 5

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
