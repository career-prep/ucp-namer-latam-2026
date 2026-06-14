# Question 8: CoinChange
# Given a list of coin denominations and a target sum k, return the number of
# possible ways to make change for that sum.

def coin_change(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]
    return dp[target]


print(coin_change([2, 5, 10], 20))
print(coin_change([2, 5, 10], 15))
print(coin_change([1, 2, 5], 5))
print(coin_change([3], 2))


# Spent 20 mins
# Time Complexity: O(k * c), where k is the target and c is the number of coins.
# Space Complexity: O(k)
