# Technique: Dynamic programming (tabulation)
# dp[amount] = ways to make amount; coins on the outer loop -> combinations not permutations
# Time: O(len(coins) * k)
# Space: O(k)


def coinChange(coins, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]
    return dp[k]


print(coinChange([2, 5, 10], 20))  # 6
print(coinChange([2, 5, 10], 15))  # 3

# Time spent: ~30 minutes