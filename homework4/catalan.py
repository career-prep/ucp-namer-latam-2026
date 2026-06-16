# Technique: Dynamic programming (tabulation)
# catalan[i] = sum of catalan[j] * catalan[i-1-j]
# Time: O(n^2)
# Space: O(n)


def catalanNumbers(n):
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    return catalan


print(catalanNumbers(1))  # [1, 1]
print(catalanNumbers(5))  # [1, 1, 2, 5, 14, 42]
print(catalanNumbers(0))  # [1]

# Time spent: ~25 minutes