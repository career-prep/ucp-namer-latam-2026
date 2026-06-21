# technique: dynamic programming - tabulation
# time complexity: O(n)
# space complexity: O(n)
# time taken: 25 mins

def minCostStairClimbing(costs):
    n = len(costs)
    # dp[i] = min cost to reach stair i
    dp = [0] * n
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, n):
        dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])

    # can exit from last or second-to-last stair
    return min(dp[n - 1], dp[n - 2])


print(minCostStairClimbing([4, 1, 6, 3, 5, 8]))        # 9
print(minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))  # 25
print(minCostStairClimbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
