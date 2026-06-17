# Question 1: MaxMeanSubArray
# Given an array of integers and an integer k, find the maximum mean of a subarray of size k.

# Examples:

# Input Array: [4, 5, -3, 2, 6, 1]
# Input k = 2
# Output: 4.5

# Input Array: [4, 5, -3, 2, 6, 1]
# Input k = 3
# Output: 3

def mean_max_subarray(arr,k):
    l,r=0,k-1
    currentSum=sum(arr[l:r+1])
    maxSum=currentSum
    while r<len(arr)-1:
        win_sum=currentSum+arr[r+1]-arr[l]
        l+=1
        r+=1
        currentSum=win_sum
        maxSum=max(win_sum,maxSum)
    return maxSum/k if k<=len(arr) else 0

print(mean_max_subarray([4, 5, -3, 2, 6, 1],3))
print(mean_max_subarray([4, 5, -3, 2, 6, 1], 2))
print(mean_max_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))
print(mean_max_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))
print(mean_max_subarray([10, -5, 3, 7, -2], 2))
print(mean_max_subarray([-1, -2, -3, -4, -5], 3))

#Time Complexity: O(n)
#Space Complexity: O(1)
#Spent 10 mins