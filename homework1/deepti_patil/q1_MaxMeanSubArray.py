def max_mean_subarray(nums, k):
    """
    Returns the maximum mean of any contiguous subarray of size k.
    Uses a sliding window to compute sums efficiently in O(n) time.
    """

    # Compute the sum of the first window of size k
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        # Remove the element leaving the window and add the new one
        window_sum += nums[i] - nums[i - k]

        # Track the maximum sum seen so far
        max_sum = max(max_sum, window_sum)

    # Convert the maximum sum into a mean
    return max_sum / k


# Example usage
print(max_mean_subarray([4, 5, -3, 2, 6, 1], 2))  # 4.5
print(max_mean_subarray([4, 5, -3, 2, 6, 1], 3))  # 3
print(max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))  # 1
print(max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))  # 1

"""
Time complexity:
- O(n) because we pass through the array once.
Space complexity:
- O(1) extra space.
"""
