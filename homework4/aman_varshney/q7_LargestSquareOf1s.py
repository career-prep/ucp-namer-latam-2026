# spent 70 minutes
# tabulation
# TC - O()
# SC - O()


def largest_sq_ones(arr: list[list[int]]) -> int:
    """Returns the side length of the largest square of 1s in a matrix."""
    if not arr or not arr[0]:
        return 0

    n = len(arr) 
    # dp = side length of square of 1s whose 
    # bottom right corner is at (i,j) 
    dp = [[0] * n for _ in range(n)]
    largest = 0 # retval

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0: # Skip 0s
                continue

            # Increment if top, left, and top left are 1s
            if i == 0 or j == 0: # To prevent out of bounds
                dp[i][j] = 1
            else: 
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

            # Update largest
            largest = max(largest, dp[i][j])

    return largest


def run_tests() -> None:
    print("Running tests")

    arr1 = [
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
    ]
    assert largest_sq_ones(arr1) == 2

    arr2 = [
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0],
    ]
    assert largest_sq_ones(arr2) == 3

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
