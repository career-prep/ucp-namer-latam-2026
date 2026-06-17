# Runtime: O(nk) where n is the # of coins
# Space complexity: O(k)
# Technique: DP Tabulization
def coinChange(k, coins):
    dp = [0] * (k+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k+1):
            dp[i] = dp[i] + dp[i-coin]
    return dp[k]


print(coinChange(20, [2,5,10]) == 6)
print(coinChange(15, [2,5,10]) == 3)
print(coinChange(10, [0]) == 0)
print(coinChange(1, [1]) == 1)

# Time Spent: 35:00
