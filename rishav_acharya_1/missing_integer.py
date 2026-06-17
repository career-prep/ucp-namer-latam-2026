"""
Given a sorted array of n-1 unique integers in the range [1, n], 
find the missing integer.

Examples:
Input: [1,2,3,4,6,7], n=7 -> Output: 5
Input: [1,2,3,4,5,6,7,8,10,12], n=12 -> Output: 9
"""

def findMissingInteger(arr, n):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1
    
    return left + 1

# Time Complexity: O(log n)
# Space Complexity: O(1)


test_cases = [
    ([1,2,3,4,6,7], 7),
    ([1,2,3,4,5,6,7,8,10,12], 12)
]

for arr, n in test_cases:
    print(findMissingInteger(arr, n))
