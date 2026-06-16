#Samaksh Arora
#Question 5 - Min Cost Stair Climbing
#Dynamic programming (Tabulation)
#Time Complexity: O(n) where n is the number of stairs
#Space Complexity: O(n)
#Time Spent: 33 minutes



def minCostStairClimbing(costs):
    n = len(costs)
    if n == 0:
        return 0
    elif n == 1:
        return costs[0]

    # Create a table to store the minimum cost to reach each step
    dp = [0] * n
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, n):
        dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])

    # The minimum cost to reach the top of the stairs is the minimum of the last two entries
    return min(dp[-1], dp[-2])

#Test Cases
assert minCostStairClimbing([4, 1, 6, 3, 5, 8]) == 9
assert minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]) == 25

# Extra: 
assert minCostStairClimbing([1, 2, 3, 4, 5]) == 8
assert minCostStairClimbing([10]) == 10
