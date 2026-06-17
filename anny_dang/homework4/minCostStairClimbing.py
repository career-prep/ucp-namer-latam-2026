def minCostStair(costs):
    """
    idea:
    - use tabulation to calculate from bottom up 
    - create empty dp list with index 0 has 1 step and index 1 has 1 step 
    - for loop from step 2 to n:
        - each step gets total number of steps of two latest previous ones 
    - return steps at last index

    time: O(n)
    space: O(n)
    """
    if not costs:
        return 
    if len(costs) == 1:
        return costs[0]

    n = len(costs)
    dp = [0]*n
    dp[0], dp[1] = costs[0], costs[1]
    for i in range(2, n):
        dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])
    
    return min(dp[-1], dp[-2])

print(minCostStair([4, 1, 6, 3, 5, 8]))
print(minCostStair([11, 8, 3, 4, 9, 13, 10]))