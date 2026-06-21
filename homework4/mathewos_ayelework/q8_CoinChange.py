# technique: dynamic programming - tabulation
# time complexity: O(k * n) where k = target sum, n = number of coin denominations
# space complexity: O(k)
# time taken: 25 mins

def coinChange(coins, target):
    # dp[i] = number of ways to make change for sum i
    dp = [0] * (target + 1)
    dp[0] = 1  # one way to make sum 0: use no coins

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]


print(coinChange([2, 5, 10], 20))  # 6
print(coinChange([2, 5, 10], 15))  # 3
print(coinChange([1, 2, 5], 10))   # 10
print(coinChange([2], 3))          # 0
