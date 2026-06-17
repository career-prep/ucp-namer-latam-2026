# Dynamic Programming - Tabulation (Bottom-Up)
# O(n) Time Complexity
# O(n) Space Complexity
# A staircase on a hiking trail implements a rather unusual toll system to cover trail maintenance costs. 
# Each stair in the staircase has a different toll which you only have to pay if you step on that stair. 
# Due to the height of the stairs, you can only climb one or two stairs at once. 
# This means that from the ground you must initially step on either stair 0 or stair 1 and that, if there are n stairs, 
# the last stair you step on can be either stair n-1 or n-2. Given an array representing the costs per stair, 
# what is the minimum possible toll you can pay to climb the staircase?


def minCostStairClimbing(tolls):

    # tolls[i] gives the cost to step on stair 'i'

    # If there are no tolls, then you do not have to pay anything
    if not tolls:
        return 0
    
    # If only one stair has a toll, and since we can climb two stairs at once, just skip that stair and not pay anything
    if len(tolls) == 1:
        return 0
    
    # If we only have two stairs, step on the cheaper of the two stairs
    if len(tolls) == 2:
        return min(tolls[0], tolls[1])
    

    # I'm thinking that we can use tabulation to calculate the minimum cost to step on each stair, up until stair n - 1
    # Once we have the min cost for each step, we return min(cost[n-1], cost[n-2])
    
    # Since we can either move 1 step or 2 steps at a time, in order to calculate the min cost for the current stair, I need the 
    # tolls for the previous two stairs.

    n = len(tolls)
    dp = [float('inf')] * n
    dp[0] = tolls[0]
    dp[1] = tolls[1]

    # To reach stair 2 (which is really the 3rd stair), we can either come from stair 0 or stair 1. In order to minimize costs,
    # we should come from the cheaper stair.
    # Therefore we can calulate the min cost to reach stair 2 with: dp[2] = tolls[2] + min(dp[0], dp[1])


    for i in range(2, n):
        dp[i] = tolls[i] + min(dp[i-2], dp[i-1])


    return min(dp[n-1], dp[n-2])


# 21 minutes


# Test Cases

tolls1 = [4, 1, 6, 3, 5, 8]

tolls2 = [11, 8, 3, 4, 9, 13, 10]

tolls3 = []

tolls4 = [999]

tolls5 = [999, 2]


print(minCostStairClimbing(tolls1))
print(minCostStairClimbing(tolls2))
print(minCostStairClimbing(tolls3))
print(minCostStairClimbing(tolls4))
print(minCostStairClimbing(tolls5))
