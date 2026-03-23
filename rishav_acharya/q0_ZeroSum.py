"""
Q0: Zero Sum Pairs
Given an array of integers, find the number of pairs that sum to zero.
Part 1: Each element can be used at most once
Part 2: Elements can be reused in different pairs (but pairs must use different indices)
"""

def zero_sum_once(arr):
    """
    Find pairs that sum to zero where each element is used at most once.
    
    Algorithm:
    - Use a dictionary to track which numbers we've encountered
    - For each number, check if its negative exists in our tracker
    - If found, we have a pair; remove the complement to prevent reuse
    - Otherwise, add current number to tracker
    """
    tracker = {}
    pair_count = 0
    
    for num in arr:
        complement = -num
        
        # Check if complement exists and hasn't been used
        if complement in tracker and tracker[complement] > 0:
            pair_count += 1
            tracker[complement] -= 1  # Mark as used
        else:
            # Add current number to tracker
            tracker[num] = tracker.get(num, 0) + 1
    
    return pair_count

# Time Complexity: O(n) - single pass through array
# Space Complexity: O(n) - dictionary storage


def zero_sum_unlimited(arr):
    """
    Find all possible pairs that sum to zero (elements can be in multiple pairs).
    
    Algorithm:
    - Maintain frequency count of all elements seen so far
    - For each element, add the frequency of its complement (all previous complements form pairs)
    - Update frequency of current element
    """
    frequency = {}
    total_pairs = 0
    
    for num in arr:
        complement = -num
        
        # Add count of how many times complement appeared before
        if complement in frequency:
            total_pairs += frequency[complement]
        
        # Update frequency of current number
        frequency[num] = frequency.get(num, 0) + 1
    
    return total_pairs

# Time Complexity: O(n) - single traversal
# Space Complexity: O(n) - frequency map storage


if __name__ == "__main__":
    test1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    test2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
    test3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    test4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
    
    print("Test with at most once:", zero_sum_once(test4))
    print("Test with unlimited reuse:", zero_sum_unlimited(test4))

# Time spent: 40 minutes
