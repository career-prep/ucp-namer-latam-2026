# Technique: Dynamic programming (tabulation)
# Time Complexity: O(C * k)
# Space Complexity: O(k)

def count_change(coins, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]
    return dp[k]

print(count_change([2, 5, 10], 20))
print(count_change([2, 5, 10], 15))
print(count_change([2, 5, 10], 0))
print(count_change([2], 3))
print(count_change([1, 2, 3], 4))

# Time spent: 10
