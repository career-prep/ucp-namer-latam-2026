# Technique: Tabulation
# Time Complexity: O(coins * k)
# Space Complexity: O(k)

def coin_change_ways(coins, k):
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]

    return dp[k]


def main():
    coins = [2, 5, 10]

    print(coin_change_ways(coins, 20))  # 6
    print(coin_change_ways(coins, 15))  # 3


if __name__ == "__main__":
    main()
    
#Time : 35 min