"""
Q1: Unique Sum
Given an array of integers, return the sum of all unique elements.
An element is unique if it appears exactly once or if we only count its first occurrence.
"""

def unique_sum(arr):
    """
    Calculate sum of unique elements in array.
    
    Algorithm:
    - Use a set to track which elements we've already added
    - Iterate through array once
    - Only add element to sum if we haven't seen it before
    - Mark element as seen
    """
    already_added = set()
    total = 0
    
    for num in arr:
        # Only process if this is first time seeing this number
        if num not in already_added:
            total += num
            already_added.add(num)
    
    return total

# Time Complexity: O(n) - iterate through array once
# Space Complexity: O(n) - set to store unique elements


if __name__ == "__main__":
    arr1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    arr2 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    
    print("Sum of unique elements in arr1:", unique_sum(arr1))
    print("Sum of unique elements in arr2:", unique_sum(arr2))

# Time spent: 12 minutes
