# Given an array of integers, return the sum of unique elements in the array.

# Examples:

# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 33

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 35
def unique_sum(arr):
    return sum(set(arr)) 
print(unique_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))

#Time Complexity= O(n)
#Space Complexity= O(n)
#Spent 10 minutes