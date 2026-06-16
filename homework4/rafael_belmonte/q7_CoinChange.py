# Technique: Dynamic programming - tabulation
# time complexity: O(k * c) where c is the number of coins
# space complexity: O(k)

def coin_change(coins, k):
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]
    return dp[k]

#test cases
assert coin_change([2, 5, 10], 20) == 6
assert coin_change([2, 5, 10], 15) == 3
assert coin_change([1, 2, 5], 5) == 4
assert coin_change([2], 3) == 0

# edge cases
assert coin_change([1], 0) == 1
assert coin_change([], 5) == 0
assert coin_change([5, 10], 3) == 0
assert coin_change([3, 5, 7], 10) == 2
assert coin_change([1, 3, 4], 6) == 4

print("yay!!")

# Time spent: ~20 minutes
