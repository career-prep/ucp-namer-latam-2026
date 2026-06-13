# Question 8: CoinChange

# Technique: Dynamic programming (tabulation)
# Classic unbounded knapsack / "number of ways" variant.
# dp[j] = number of ways to make change for amount j.
# dp[0] = 1 (one way to make 0: use no coins).
# For each coin denomination, iterate amounts from coin to k and add dp[j-coin].
# Outer loop over coins ensures each combination is counted once (not permutations).

# Time Complexity:  O(k * C) where k = target sum, C = number of coin types
# Space Complexity: O(k)


def coinChange(coins, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, k + 1):
            dp[j] += dp[j - coin]
    return dp[k]
# Time Complexity = O(k * C), Space Complexity = O(k)


# --- Tests ---

print("Coins [2,5,10], sum=20:", coinChange([2, 5, 10], 20))
# Expected: 6

print("Coins [2,5,10], sum=15:", coinChange([2, 5, 10], 15))
# Expected: 3

print("Coins [1,2,3], sum=4:", coinChange([1, 2, 3], 4))
# Expected: 4 (1+1+1+1, 1+1+2, 2+2, 1+3)

print("Coins [2], sum=3:", coinChange([2], 3))
# Expected: 0 (can't make 3 with only 2s)

print("Coins [5], sum=0:", coinChange([5], 0))
# Expected: 1 (empty set)

# Spent a total of 20 mins on this question
