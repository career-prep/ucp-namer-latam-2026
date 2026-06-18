# spent 20 minutes
# tabulation
# TC - O(n)
# SC - O(n)


def min_cost_climbing_stairs(arr: list[int]) -> int:
    """Returns the minimum toll to climb the staircase."""
    # Degen base cases
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # dp[i] = min cost to step on stair i
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[1]

    # dp[i] = stair cost for i + minimum path cost
    for i in range(2, n):
        dp[i] = arr[i] + min(dp[i-1], dp[i-2])

    # Finish on the last or second last stair
    return min(dp[n-1], dp[n-2])



def run_tests():
    print("Running tests")

    input1 = [4, 1, 6, 3, 5, 8]
    expected1 = 9
    assert min_cost_climbing_stairs(input1) == expected1

    input2 = [11, 8, 3, 4, 9, 13, 10]
    expected2 = 25
    assert min_cost_climbing_stairs(input2) == expected2

    print("All tests passed")

if __name__ == "__main__":
    run_tests()
