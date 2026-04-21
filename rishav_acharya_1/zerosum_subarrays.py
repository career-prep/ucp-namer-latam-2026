"""
Given an array of integers, count the number of subarrays that sum to zero.

Examples:
Input: [4, 5, 2, -1, -3, -3, 4, 6, -7] -> Output: 2
Input: [1, 8, 7, 3, 11, 9] -> Output: 0
Input: [8, -5, 0, -2, 3, -4] -> Output: 2
"""

def countZeroSumSubarrays_brute(arr):
    count = 0
    
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == 0:
                count += 1
    
    return count

# Time Complexity: O(n^2)
# Space Complexity: O(1)


def countZeroSumSubarrays_optimal(arr):
    prefix_sum = 0
    count = 0
    sum_freq = {0: 1}
    
    for num in arr:
        prefix_sum += num
        
        if prefix_sum in sum_freq:
            count += sum_freq[prefix_sum]
            sum_freq[prefix_sum] += 1
        else:
            sum_freq[prefix_sum] = 1
    
    return count

# Time Complexity: O(n)
# Space Complexity: O(n)


test_cases = [
    [4, 5, 2, -1, -3, -3, 4, 6, -7],
    [1, 8, 7, 3, 11, 9],
    [8, -5, 0, -2, 3, -4]
]

print("Brute Force:")
for test in test_cases:
    print(countZeroSumSubarrays_brute(test))

print("\nOptimal:")
for test in test_cases:
    print(countZeroSumSubarrays_optimal(test))
