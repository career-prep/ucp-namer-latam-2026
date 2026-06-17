# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(n^2) since we have nested loops
# Space Complexity: O(n) since we have to store the DP table

def catalan(n: int) -> list[int]:
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    
    return dp

print(catalan(1))
print(catalan(5))

# Time Spent: 29 minutes