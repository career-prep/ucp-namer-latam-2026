# Technique: One-directional running computation/total
# Time Complexity: O(n)
# Space Complexity: O(n)

def zero_sum_subarray(nums):
    left_sum = 0
    counts = 0
    seen = {0: 1}

    for i in range(len(nums)):
        left_sum += nums[i]

        if left_sum in seen:
            counts += seen[left_sum]
            seen[left_sum] += 1
        else:
            seen[left_sum] = 1

    return counts

print(zero_sum_subarray([4,5,2,-1,-3,-3,4,6,-7]))
print(zero_sum_subarray([1,8,7,3,11,9]))
print(zero_sum_subarray([8,-5,0,-2,3,4]))

# My Edge test cases:
print(zero_sum_subarray([])) # empty list
print(zero_sum_subarray([0])) # single element

# Time Spent: 18mins 30secs