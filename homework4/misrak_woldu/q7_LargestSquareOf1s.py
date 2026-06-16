# Technique: Dynamic Programming - Tabulation
# Data Structure: Matrix / 2D Array
# Time Complexity: O(rows * cols)
# Space Complexity: O(rows * cols)


def largest_square_of_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    row_count = len(matrix)
    col_count = len(matrix[0])

    dp = [[0] * col_count for _ in range(row_count)]

    largest_square_size = 0

    for row_index in range(row_count):
        for col_index in range(col_count):
            if matrix[row_index][col_index] == 1:
                if row_index == 0 or col_index == 0:
                    dp[row_index][col_index] = 1
                else:
                    dp[row_index][col_index] = 1 + min(
                        dp[row_index - 1][col_index],      # above
                        dp[row_index][col_index - 1],      # left
                        dp[row_index - 1][col_index - 1],  # diagonal
                    )

                largest_square_size = max(
                    largest_square_size,
                    dp[row_index][col_index],
                )

    return largest_square_size


def run_tests() -> None:
    assert largest_square_of_ones([
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
    ]) == 2

    assert largest_square_of_ones([
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0],
    ]) == 3

    assert largest_square_of_ones([]) == 0

    assert largest_square_of_ones([[]]) == 0

    assert largest_square_of_ones([
        [0, 0],
        [0, 0],
    ]) == 0

    assert largest_square_of_ones([
        [1, 1],
        [1, 1],
    ]) == 2

    assert largest_square_of_ones([
        [1],
    ]) == 1

    assert largest_square_of_ones([
        [0],
    ]) == 0

    assert largest_square_of_ones([
        [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]) == 2

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
