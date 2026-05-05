"""
Technique Used: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)

Intuition: Since the array is sorted, we can use binary search to find the missing value. 
Use binary search so we don't need to search the entire array. 
"""

def MissingInteger(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1
    return left + 1

test = [([1, 2, 3, 5, 6, 7], 7),
        ([1], 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12),
        ]

for i in test:
    print(MissingInteger(i[0], i[1]))

# Time Spent: 15 mins