# Technique: Dynamic programming (tabulation)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def catalan_numbers(n):
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for k in range(n):
        for i in range(k + 1):
            catalan[k + 1] += catalan[i] * catalan[k - i]
    return catalan

print(catalan_numbers(0))
print(catalan_numbers(1))
print(catalan_numbers(5))
print(catalan_numbers(9))

# Time spent: 15
