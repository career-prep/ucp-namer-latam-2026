# Technique: Binary Search variation
# Time Complexity: O(log n)
# Space Complexity: O(1)

def missing_integer(nums, n):
    l, r = 0, len(nums)

    while l < r:
        m = (l + r) // 2

        if nums[m] == m + 1:
            l = m + 1
        else:
            r = m

    return l + 1 if l < n else n

print(missing_integer([1,2,3,4,6,7], 7))
print(missing_integer([1], 2))
print(missing_integer([1,2,3,4,5,6,7,8,10,11,12], 12))

# My Edge Testcase:
print(missing_integer([], 1)) # empty array

# Time Taken: 7mins 19secs