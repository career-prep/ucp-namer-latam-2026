# Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.
# Examples:
# Input Array: [4, 5, -3, 2, 6, 1]
# Input k = 2
# Output: 4.5
# Input Array: [4, 5, -3, 2, 6, 1]
# Input k = 3|
# Output: 3
# Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1]
# Input k = 3
# Output: 1
# Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
# Input k = 5
# Output: 1

# Technique- 2 pointers fixed sized sliding window 
# time- 35 mins
# time and space complexity- initilly we have sum of k number which is o(k) + then we have sliding window loop which runs at o(n-k) which is o(n)-> so time complexity is  o(k) + o(n) == o(n)

def maxmean(arr, k):
    if len(arr) < k:
        return None

    sum_window = sum(arr[:k]) 
    max_sum = sum_window

    for i in range(k, len(arr)):
        sum_window = sum_window + arr[i] - arr[i - k]       
        max_sum = max(max_sum, sum_window)

    mean = max_sum / k

    if mean.is_integer():
        return int(mean)
    return mean

    return max_sum / k

print(maxmean([4, 5, -3, 2, 6, 1], 2))
print(maxmean([4, 5, -3, 2, 6, 1], 3))
print(maxmean([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))
print(maxmean([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))