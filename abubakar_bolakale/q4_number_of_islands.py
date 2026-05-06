# Data structure: Graph (implicit grid)
# Algorithm: Depth-first search


def num_islands(grid):
    if not grid:
        return 0
    n, m = len(grid), len(grid[0])
    islands = 0

    def sink(i, j):
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
            return
        grid[i][j] = 0
        sink(i + 1, j)
        sink(i - 1, j)
        sink(i, j + 1)
        sink(i, j - 1)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                islands += 1
                sink(i, j)
    return islands


def cp(g):
    return [r[:] for r in g]


if __name__ == "__main__":
    print("=== Handout strip 6x1 -> 1 island ===")
    strip = [[1], [0], [0], [0], [0], [0]]
    print(" ", num_islands(cp(strip)))

    print("=== Handout-style 5x5 (row-major 1s) -> 2 islands (interpretation as 5 columns) ===")
    g5 = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    print(" ", num_islands(cp(g5)))

    print("=== Full land ===")
    print(" ", num_islands(cp([[1, 1], [1, 1]])))

    print("=== All water ===")
    print(" ", num_islands(cp([[0, 0], [0, 0]])))

    print("=== Empty grid ===")
    print(" ", num_islands([]))

    print("=== Four corners ===")
    four = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(" ", num_islands(cp(four)))

    print("=== Single cell land ===")
    print(" ", num_islands(cp([[1]])))


# Time complexity: O(R * C)
# Space complexity: O(R * C)
# Time spent: 35 minutes
