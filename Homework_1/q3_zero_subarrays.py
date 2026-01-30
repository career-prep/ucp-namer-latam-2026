# Question 3: ZeroSumSubArrays

# Given an array of integers, count the number of subarrays that sum to zero.

# Examples:

# Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7] 
# Output: 2 (Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

# Input Array: [1, 8, 7, 3, 11, 9] 
# Output: 0

# Input Array: [8, -5, 0, -2, 3, -4] 
# Output: 2 (Subarrays: [0], [8, -5, 0, -2, 3, -4])

def zero_subarray(arr):
    count=0
    
    for l in range(len(arr)):
        curr_sum=0
        for r in range(l,len(arr)):
            curr_sum+=arr[r]
            if curr_sum==0:
                count+=1
    
    return count

print(zero_subarray([1, 8, 7, 3, 11, 9]))
print(zero_subarray([8, -5, 0, -2, 3, -4]))
print(zero_subarray([8, -5, 0, -2, 3, -4]))
print(zero_subarray([0, 0, 0, 0]))
print(zero_subarray([1, 2, 3, 4, 5]))
print(zero_subarray([5, -5, 3, -3, 1, -1]))
print(zero_subarray([1, -1, 1, -1, 1, -1]))
print(zero_subarray([0]))
print(zero_subarray([10, -5, -5, 8, -8]))


#Time Complexity: O(n^2)
#Space Complexity: O(1)
#Spent 10 mins