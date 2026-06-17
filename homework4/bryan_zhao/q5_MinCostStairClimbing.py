# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(n) since we pass through the cost list once
# Space Compelexity: O(1) since we are only keeping track of two shifting variables

def min_cost_stair_climbing(cost: list[int]) -> int:
    prev2 = cost[0] # dp[i-2]
    prev1 = cost[1] # dp[i-1]

    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr
    
    return min(prev1, prev2)


cost1 = [4, 1, 6, 3, 5, 8]
print(min_cost_stair_climbing(cost1))

cost2 = [11, 8, 3, 4, 9, 13, 10]
print(min_cost_stair_climbing(cost2))

# Time Spent: 15 minutes