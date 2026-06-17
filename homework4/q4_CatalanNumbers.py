# Runtime: O(n^2)
# Space complexity: O(n)
# Technique: DP Tabulization
def CatalanNumbers(k):
    if k == 0:
        return [1]
    dp = [0] * (k+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, k+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp


print(CatalanNumbers(1) == [1,1])
print(CatalanNumbers(0) == [1])
print(CatalanNumbers(5) == [1, 1, 2, 5, 14, 42])

# Time Spent: 30:00
