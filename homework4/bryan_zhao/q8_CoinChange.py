# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O (N x k) where N is # of coin denominations and k is the target sum 
# Space Complexity: O(k) since we store an array of size k + 1

def coin_change(coins: list[int], k: int) -> int:
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]
    
    return dp[k]

coins = [2, 5, 10]

print(coin_change(coins, 20))
print(coin_change(coins, 15))

# Time Spent: 15 minutes