# spent 15 min
# tabulation
# TC - O(n*k) where k is target
# SC - O(k)


def coin_change(coins: list[int], target: int) -> int:
    """Returns the number of ways to make change for `target` using the given coins."""
    # dp[i] = number of ways to make sum i
    dp = [0] * (target+1)
    dp[0] = 1  # Only one way to make 0

    # For each coin, update all amounts from `coin` to `target`
    for coin in coins:
        for amount in range(coin, target+1):
            dp[amount] += dp[amount-coin]

    return dp[target]


def run_tests():
    print("Running tests")
    coins = [2, 5, 10]

    input1 = 20
    assert coin_change(coins, input1) == 6
    
    input2 = 15
    assert coin_change(coins, input2) == 3

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
