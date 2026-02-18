# Given an integer n and a sorted array of integers of size n-1 which contains 
# all but one of the integers in the range 1-n, find the missing integer.

# Examples:

# Input Array: [1, 2, 3, 4, 6, 7]
# Input n: 7
# Output: 5

# Input Array: [1]
# Input n: 2
# Output: 2

# Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
# Input n: 12
# Output: 9

def missing_number(arr,k):
    expected_sum = k * (k + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
print(missing_number([1, 2, 3, 4, 6, 7], 7))
print(missing_number([1], 2))
print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))
print(missing_number([2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
print(missing_number([1, 2, 3, 4, 5], 6))
print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(missing_number([2], 2))
print(missing_number([1, 3], 3))
print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16], 16))
print(missing_number([2, 3, 4, 5], 5))

#Time Complexity: O(n)
#Space Complexity: O(1)
#Spent 7 mins