"""
idea:
    to find the min cost at stair[i] 
    => cheapest way will be:  dp[i] = cost[i] + min(dp[i-1], dp[i-2]) 

"""

def min_cost_stair_climbing(costs):
    # num of stair
    stair_num = len(costs)

    # if only 1 step -> must use it
    if stair_num == 1:
        return costs[0]

    #dp[i] means the min cost to reach stair i
    dp = [0] * stair_num

    # start either on stair 0 or 1
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2,stair_num):

        dp[i] = costs[i] + min(dp[i-1], dp[i-2])
    

    return min(dp[stair_num-1], dp[stair_num-2])


print(min_cost_stair_climbing([4,1,6,3,5,8]))
print(min_cost_stair_climbing([11,8,3,4,9,13,10]))