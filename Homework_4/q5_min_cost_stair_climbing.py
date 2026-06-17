# Question 5: MinCostStairClimbing
# Given an array of toll costs per stair, return the minimum possible toll to
# climb the staircase when each move can climb one or two stairs. You may start
# on stair 0 or stair 1, and the final stepped stair may be n - 1 or n - 2.

def min_cost_stair_climbing(costs):
    if not costs:
        return 0
    if len(costs) == 1:
        return costs[0]
    two_back = costs[0]
    one_back = costs[1]
    for i in range(2, len(costs)):
        current = costs[i] + min(one_back, two_back)
        two_back = one_back
        one_back = current
    return min(one_back, two_back)


print(min_cost_stair_climbing([4, 1, 6, 3, 5, 8]))
print(min_cost_stair_climbing([11, 8, 3, 4, 9, 13, 10]))
print(min_cost_stair_climbing([10, 15]))
print(min_cost_stair_climbing([]))


# Spent 20 mins
# Time Complexity: O(n)
# Space Complexity: O(1)
