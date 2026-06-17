# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(len(coins) * target)
# Space Complexity: O(target)

def coin_change(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]
    return dp[target]

# Time Taken: 11mins 18secs

# Testcases:
coins_1 = [2, 5, 10]
target_1 = 20
print(coin_change(coins_1, target_1))

coins_2 = [2, 5, 10]
target_2 = 15
print(coin_change(coins_2, target_2))

#Edge cases:
coins_3 = [1, 2, 5]
target_3 = 0 #0 target
print(coin_change(coins_3, target_3))

coins_4 = [5, 10]
target_4 = 3 #Target not reachable
print(coin_change(coins_4, target_4))