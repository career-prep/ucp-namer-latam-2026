# Array/String Technique: 2a. Dynamic programming - Tabulation
# Time Complexity: O(C * A)
# Space Complexity: O(A)

def change(coins: list[int], amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
            
    return dp[amount]

if __name__ == "__main__":
    print("Ways to make change for 5 with [1, 2, 5]:", change([1, 2, 5], 5))

# Time Spent: 15 minutes