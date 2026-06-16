# Technique: Dynamic programming - tabulation
# time complexity: O(n^2)
# space complexity: O(n)

def catalan_numbers(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in range(i):
            total += dp[j] * dp[i - 1 - j]
        dp[i] = total
    return dp

#test cases
assert catalan_numbers(1) == [1, 1]
assert catalan_numbers(5) == [1, 1, 2, 5, 14, 42]
assert catalan_numbers(0) == [1]
assert catalan_numbers(3) == [1, 1, 2, 5]

# edge cases
assert catalan_numbers(2) == [1, 1, 2]
assert catalan_numbers(6) == [1, 1, 2, 5, 14, 42, 132]
assert len(catalan_numbers(7)) == 8
assert catalan_numbers(7)[-1] == 429

print("yay!!")

# Time spent: ~15 minutes
