"""
Time, Memory complexities: O(n), O(1)

Q1:
Given an array of integers and an integer, k, find the maximum mean of a subarray 
of size k.

Examples:
Input Array: [4, 5, -3, 2, 6, 1], k = 2
Output: 4.5

Input Array: [4, 5, -3, 2, 6, 1], k = 3
Output: 3
"""

def MaxMeanSubArray(arr, k):
    #1. Edge case
    if len(arr) < k:
        return 0

    #2. Basing approach on sums to avoid decimals and calculating first window
    current_sum = sum(arr[:k])
    max_sum = current_sum

    #3. Iterating over array from k to the end
    for i in range(k, len(arr)):
        #4. Moves sliding window by removing element leaving and adding the 
        # entering one
        current_sum = current_sum - arr[i-k] + arr[i]

        #5. Update max sum seen
        max_sum = max(max_sum, current_sum)

    #6. Return result
    return max_sum / k

def test_MMSA():
    input_array = [4, 5, -3, 2, 6, 1] 
    k = 2
    expected = 4.5
    result = MaxMeanSubArray(input_array, k)
    assert result == expected, f"Expected {expected}, got {result}"

    input_arr = [4, 5, -3, 2, 6, 1]
    k = 3
    expected = 3.0
    result = MaxMeanSubArray(input_arr, k)
    assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_MMSA()