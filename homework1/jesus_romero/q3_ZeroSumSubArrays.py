"""
Time, Space complexities: O(n), O(n) 

Q3: ZeroSumSubArrays
Given an array of integers, count the number of subarrays that sum to zero

input_array = [4, 5, 2, -1, -3, -3, 4, 6, -7]
output = 2
subarrays = [[5, 2, -1, -3, -3], [-3, 4, 6, -7]]

input_array = [1, 8, 7, 3, 11, 9]
output = 0

input_array = [8, -5, 0, -2, 3, -4]
output = 2
subarrays = [[0], [8, -5, 0, -2, 3, -4]]
"""

def countZeroSumSubarrays(nums):
    #1. Map to store how many times a prefix sum has occurred
    # starting with {0: 1} to handle subarrays starting at index 0
    prefix_map = {0: 1}
    running_sum = 0
    count = 0
    
    #2. Iterate over numbers 
    for num in nums:
        running_sum += num
        
        # 3. If the running_sum exists in map, it means the elements between 
        # the previous occurrence and here sum to 0
        if running_sum in prefix_map:
            count += prefix_map[running_sum]
            prefix_map[running_sum] += 1
        else:
            prefix_map[running_sum] = 1
            
    return count

def test_CZSS():
    input_array = [4, 5, 2, -1, -3, -3, 4, 6, -7]
    expected = 2
    result = countZeroSumSubarrays(input_array)
    assert result == expected, f"Expected {expected}, got {result}"

    input_array = [1, 8, 7, 3, 11, 9]
    expected = 0
    result = countZeroSumSubarrays(input_array)
    assert result == expected, f"Expected {expected}, got {result}"

    input_array = [8, -5, 0, -2, 3, -4]
    expected = 2
    result = countZeroSumSubarrays(input_array)
    assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_CZSS()

