"""
Given an array of integers, return the sum of unique elements in the array

Example: 
Input: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
Expected Output: 33

Input: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
Expected Output: 35
"""


def unique_sum(num):
    my_map = {}
    total = 0

    for number in num:
        my_map[number] = my_map.get(number, 0) + 1

        if my_map.get(number) == 1:
            total += number

    return total


print(unique_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(unique_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))
