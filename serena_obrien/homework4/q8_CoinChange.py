# Time complexity: O(n*k)
# Space complexity: O(k)

# Technique: Dynamic programming: tabulation

def CoinChange(coins: list, k: int):
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]

    return dp[k]

if __name__ == "__main__":
    coins = [2, 5, 10]

    targets = [0, 20, 15]

    for t in targets:
        print(f"Number of ways to sum to {t}: {CoinChange(coins, t)}")

# ~ time spent: ~30 minutes