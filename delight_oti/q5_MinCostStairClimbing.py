# Technique: Dynamic programming - Tabulation

def MinCostStairClimbing(cost):

    n = len(cost)

    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):

        one_step_before = dp[i - 1]
        two_steps_before = dp[i - 2]

        dp[i] = cost[i] + min(one_step_before, two_steps_before)

    return min(dp[n - 1], dp[n - 2])


# print(MinCostStairClimbing([4, 1, 6, 3, 5, 8]))
# Output: 9

# print(MinCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))
# Output: 25