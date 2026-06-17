# Runtime: O(n)
# Space complexity: O(n)
# Technique: DP Tabulization
def minCostStairClimbing(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    dp = [0] * (n)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])

print(minCostStairClimbing([4, 1, 6, 3, 5, 8]) == 9)
print(minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]) == 25)
print(minCostStairClimbing([]) == 0)
print(minCostStairClimbing([67]) == 67)

# Time Spent: 10:00
