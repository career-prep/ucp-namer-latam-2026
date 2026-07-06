# Method: Dynamic Programming (Tabulation)
# Time Complexity: O(N)
# Space Complexity: O(N)
# Total Time Taken: 30 mins

def MinCostStairClimbing(cost):
    n = len(cost)
    # Edge Case
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
        
    DP = [0] * (n + 1)
    
    # Base cases Starting at step 0 or step 1 costs 0
    DP[0] = 0
    DP[1] = 0
    
    for i in range(2, n + 1):
        DP[i] = min(DP[i - 1] + cost[i - 1], DP[i - 2] + cost[i - 2]) # Min cost is either i-1 or i-2
        
    return DP[n]

print(MinCostStairClimbing([4, 1, 6, 3, 5, 8]))
print(MinCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))
print(MinCostStairClimbing([10, 15, 20]))  
print(MinCostStairClimbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) 