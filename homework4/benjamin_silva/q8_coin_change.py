def coin_change(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[target]


if __name__ == "__main__":
    print(coin_change([2, 5, 10], 20))  
    print(coin_change([2, 5, 10], 15))  
    print(coin_change([2, 5, 10], 0))   
    print(coin_change([3], 7))         
    print(coin_change([1], 5))          

    # Time spent: 20 minutes