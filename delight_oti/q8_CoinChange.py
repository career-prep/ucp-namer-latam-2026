# Technique: Dynamic programming - Tabulation

def CoinChange(coins, target):

    dp = [0] * (target + 1)

    dp[0] = 1

    for coin in coins:

        for amount in range(coin, target + 1):

            previous_amount = amount - coin

            dp[amount] = dp[amount] + dp[previous_amount]

    return dp[target]

# coins = [2, 5, 10]

# print(CoinChange(coins, 20))
# Output: 6

# print(CoinChange(coins, 15))
# Output: 3