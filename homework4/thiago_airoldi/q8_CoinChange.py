# Dynamic Programming - Tabulation
# O(c * n) Time Complexity, where c is the number of coins and n is the target
# O(n) Space Complexity, where n is the target
# Given a list of coin denominations and a target sum k, return the number of possible ways to make change for that sum.

def coinChange(coins, target):

    # If we choose no coins, that's one way to reach a target of zero.
    if target == 0:
        return 1
    
    # If we have no coins and target > 0, we cannot reach the target
    if not coins:
        return 0
    

    # I would ask in an interview if I should return 0 or -1 to signify if I cannot reach the target with the given coins in any combination.
    # I will assume that returning 0 is fine, since that's like saying "There are zero ways to use these given coins to reach the target."

    # My intuition is to use tabulation and fill the dp array bottom up. 

    # The base case for a target of 0 is 1, so I can fill a dp array in which dp[i] gives you the number of ways to reach the target 'i' using the given coins.
    # So dp[0] = 1 always.

    dp = [0] * (target + 1)
    dp[0] = 1

    # To fill up the dp array bottom up, for each coin, we need to check how many ways we can reach a previous value we already calculated that is inside the array
    # by using that specific coin.
    for coin in coins:

        # The iterator 'i' will act as the current value we are on
        for i in range(1, target + 1): # We can skip the 0 value because we already filled it inside the dp array

            currValue = i # Redundant, but I will use this for clarity

            prevValue = currValue - coin

            # Since we are filling bottom-up, as long as prevValue is at least 0, it should have a valid number of ways to reach that value in our dp array
            if prevValue >= 0:
                dp[currValue] += dp[prevValue]


    return dp[target]



# 29 minutes


# Test Cases

coins1 = [2, 5, 10]
coins2 = []

target1 = 20
target2 = 15
target3 = 0

print(coinChange(coins1, target1))
print(coinChange(coins1, target2))
print(coinChange(coins2, target2))
print(coinChange(coins1, target3))




