# Question 4: Catalan Numbers
# The nth Catalan number is defined as (2n)! / ((n + 1)!n!). Given a
# non-negative integer n, return the Catalan numbers from 0 through n.

def catalan_numbers(n):
    if n < 0:
        return []
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in range(i):
            total += dp[j] * dp[i - 1 - j]
        dp[i] = total
    return dp


print(catalan_numbers(1))
print(catalan_numbers(5))
print(catalan_numbers(0))
print(catalan_numbers(7))


# Spent 20 mins
# Time Complexity: O(n^2)
# Space Complexity: O(n)
