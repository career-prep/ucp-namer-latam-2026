# This is a dp problem

# Really didn't know where to get started with this problem
# Looked at the neetcode algorithm description but did not look at any code implementations

# The approach
# Bottom up memoization using recursion

# Idea
"""
Given coins = [1,2,5] and sum = 5

We want to count the number of combinations that add up to 5

At each coin, we have 2 choices:
1. Use the coin again
2. Move on to the next coin

If we "skip" a coin we can avoid permutations or duplicates of the same answer 
by never going back to that index
"""
# I think the time complexity is O(n*m) where m is the sum O(n*m) space too
def coinChange(coins, sum):
    memo = {}

    def helper(index, remaining):
        if remaining == 0:
            return 1
        if remaining < 0 or index == len(coins):
            return 0

        key = (index, remaining)

        if key in memo:
            return memo[key]

        left_subproblem = helper(index,remaining - coins[index])
        right_subproblem = helper(index+1, remaining)

        memo[key] = left_subproblem + right_subproblem

        return memo[key]

    return helper(0,sum)


# Test case
test1 = coinChange([1,2,5], 5)
print(test1)

#This took me over the allotted 40 minutes