# Technique: Fixed-size sliding window
# Time Complexity: O(n)
# Space Complexity: O(n)

def max_mean_subarray(arr, k):
    if not arr or k <= 0: # return None for invalid parameters
        return None
    left = 0
    best = float("-inf") # to handle negative numbers also
    window_sum = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        if right - left + 1 == k:
            mean = window_sum / k
            best = max(best, mean)
            window_sum -= arr[left]
            left += 1

    return best

print(max_mean_subarray([4,5,-3,2,6,1], 2))
print(max_mean_subarray([4,5,-3,2,6,1], 3))
print(max_mean_subarray([1,1,1,1,-1,-1,2,-1,-1], 3))
print(max_mean_subarray([1,1,1,1,-1,-1,2,-1,-1,6], 5))

# My Edge Testcases:
print(max_mean_subarray([], 3)) # Empty Array
print(max_mean_subarray([4,5,-3,2,6,1], 0)) # k is less than 1
print(max_mean_subarray([-4, -1, -4, -2, -3, -6], 3)) # Negative Numbers

# Time Spent: 6mins 41secs