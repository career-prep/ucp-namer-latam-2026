def count_zero_sum_subarrays(nums):
    """
    Count the number of contiguous subarrays whose sum is 0.

    So every time we see the same prefix sum again, it means
    there are as many zero-sum subarrays ending here as the number
    of times we've seen this prefix sum before.

    Time Complexity: O(n)
        - One pass through the array, O(1) average hashmap operations.
    Space Complexity: O(n)
        - Hashmap can store up to n distinct prefix sums.
    """

    prefix_sum = 0
    count = 0

    # Map: prefix_sum_value -> how many times we've seen it so far
    seen = {0: 1}
    # Start with 0 seen once because a prefix_sum of 0 means
    # the subarray from index 0 to current index sums to 0.

    for x in nums:
        prefix_sum += x

        # If we've seen this prefix sum before, each previous occurrence
        # forms a zero-sum subarray ending at the current index.
        count += seen.get(prefix_sum, 0)

        # Record that we've now seen this prefix sum one more time
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


# Example usage
print(count_zero_sum_subarrays([4, 5, 2, -1, -3, -3, 4, 6, -7]))  # 2
print(count_zero_sum_subarrays([1, 8, 7, 3, 11, 9]))             # 0
print(count_zero_sum_subarrays([8, -5, 0, -2, 3, -4]))           # 2

