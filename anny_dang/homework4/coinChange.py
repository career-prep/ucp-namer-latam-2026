def coinChange(coins, k):
    """
    idea:
    - create a dp with k + 1 in length -> dp[amount] stores how many ways
    we can make that amount using coins processed so far 
    - set dp[0] = 1 because there is 1 way to make 0 (no coins used)
    - for each coin, update all amounts from coin to target
        - dp[amount] += dp[amount - coin] 

    time: O(n * k) (n: number of coins, k : target sum)
    space: O(k)
    """
    dp = [0]*(k + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[k]
    


coins = [2, 5, 10]

print("Coins:", coins)
print("Sum: 20 ->", coinChange(coins, 20))
print("Sum: 15 ->", coinChange(coins, 15))
