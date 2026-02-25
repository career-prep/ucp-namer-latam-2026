# Question 3: ZeroSumSubArrays
# Given an array of integers, count the number of subarrays that sum to zero.
# Examples:
# Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
# Output: 2
# (Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])
# Input Array: [1, 8, 7, 3, 11, 9]
# Output: 0
# Input Array: [8, -5, 0, -2, 3, -4]
# Output: 2
# (Subarrays: [0], [8, -5, 0, -2, 3, -4])

# time - complexity - o(N^2)
# time- 8 min 

def zerosum(arr):
    n = len(arr)
    count = 0

    for i in range(n):         
        current_sum = 0
        for j in range(i, n):  
            current_sum += arr[j]

            if current_sum == 0:
                count += 1

    return count
print(zerosum([4, 5, 2, -1, -3, -3, 4, 6, -7]))

# in o(N)
