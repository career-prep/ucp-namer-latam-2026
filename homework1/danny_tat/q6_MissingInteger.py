"""
Given an integer n and a sorted array of integers of size n-1 which contains all but one 
of the integers in the range 1-n, find the missing integer

Input Array: [1, 2, 3, 4, 6, 7], Input n: 7
Output: 5


Input Array: [1], Input n: 2
Output: 2

Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], Input n: 12
Output: 9
"""


def missingInteger(array, size):
    n = len(array)
    map = {}

    for i in range(n):
        map[array[i]] = map.get(array[i], 0) + 1

    for i in range(1, size + 1):
        if i not in map:
            return i


print(missingInteger([1, 2, 3, 4, 6, 7], 7))
print(missingInteger([1], 2))
print(missingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))
