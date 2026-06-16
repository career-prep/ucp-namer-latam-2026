# Technique: Dynamic programming (tabulation)
# dp[i] = cheapest toll to stand on stair i; finish on the last or second-last stair
# Time: O(n)
# Space: O(n)


def minCostStairClimbing(cost):
    n = len(cost)
    if n <= 1:
        return cost[0] if n == 1 else 0

    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])


print(minCostStairClimbing([4, 1, 6, 3, 5, 8]))        # 9
print(minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))  # 25

# Time spent: ~25 minutes