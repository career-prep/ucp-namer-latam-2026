# Question 4: Catalan Numbers

# Technique: Dynamic programming (tabulation)
# Use the recurrence C(0) = 1, C(n) = sum(C(i) * C(n-1-i)) for i in 0..n-1.
# This is equivalent to the closed-form (2n)!/((n+1)!*n!) but avoids large
# factorial arithmetic and naturally builds up a table of all values 0..n.

# Time Complexity:  O(n^2) — filling n values, each needing O(n) work
# Space Complexity: O(n) for the dp table


def catalanNumbers(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp
# Time Complexity = O(n^2), Space Complexity = O(n)


# --- Tests ---

print("n=1:", catalanNumbers(1))   # [1, 1]
print("n=5:", catalanNumbers(5))   # [1, 1, 2, 5, 14, 42]
print("n=0:", catalanNumbers(0))   # [1]
print("n=7:", catalanNumbers(7))   # [1, 1, 2, 5, 14, 42, 132, 429]

# Spent a total of 20 mins on this question
