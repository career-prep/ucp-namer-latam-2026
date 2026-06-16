# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def catalan_numbers(n):
    nums = [0] * (n + 1)
    nums[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            nums[i] += nums[j] * nums[i - 1 - j]
    return nums

# Time Taken: 8mins 39secs

# Testcases:
n_1 = 1
print(catalan_numbers(n_1))

n_2 = 5
print(catalan_numbers(n_2))

#My testcases:
n_3 = 0
print(catalan_numbers(n_3))

n_4 = 2
print(catalan_numbers(n_4))