def CoinChange(amount, denominations):
    if amount == 0:
        return 1
        
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in denominations:           
        for i in range(coin, amount + 1): 
            if coin <= i:
                dp[i] += dp[i-coin] 

    return dp[amount]

print(CoinChange(20, [2,5,10]))  
