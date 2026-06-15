#Samaksh Arora
#Question 8 - Coin Change
#Dynamic programming (Tabulation)
#Time Complexity:
#Space Complexity:
#Time Spent:



def coinChange(coins, target_sum):

    dp = [0] * (target_sum + 1)
    dp[0] = 1
    for coin in coins:
        for amount in range(coin, target_sum + 1):
            dp[amount] += dp[amount - coin]
    return dp[target_sum]

#Test Cases
assert coinChange([2, 5, 10], 20) == 6
assert coinChange([2, 5, 10], 15) == 3

# Extra: 
assert coinChange([1], 5) == 1
assert coinChange([2], 3) == 0
