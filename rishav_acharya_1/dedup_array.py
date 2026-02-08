"""
Given an array of integers, remove duplicates and return array with unique elements.

Examples:
Input: [1,2,2,3,3,3,4,4,4,4] -> Output: [1,2,3,4]
Input: [1,3,4,8,10,12] -> Output: [1,3,4,8,10,12]
"""

def removeDuplicates(arr):
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Time Complexity: O(n)
# Space Complexity: O(n)


test_cases = [
    [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    [1, 3, 4, 8, 10, 12]
]

for test in test_cases:
    print(removeDuplicates(test))
