# Technique: Fixed-size sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_mean_subarray(arr, k):
    # Edge case for empty array or invalid window size
    if not arr or k <= 0 or k > len(arr):
        return None

    left = 0
    best = float("-inf") # initial max
    window_sum = 0

    for right in range(len(arr)):
        # Expand the window by including the current element
        window_sum += arr[right]

        if right - left + 1 == k:
            mean = window_sum / k # Compute the mean
            best = max(best, mean)

            # Slide the window forward
            window_sum -= arr[left]
            left += 1
    # Return the maximum mean
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