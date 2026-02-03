# time complexity: O(n)
# space complexity: O(n)

"""
Given a array of integers, return the number of pairs of integers in the array that sum to 0 assuming 
you can use the element at each index at most once

Examples:
Input: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1] -> 
Output: 2 (Pairs: (1, -1), (2, -2))

Input: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1] -> 
Output: 3 (Pairs: (1, -1), (2, -2), (2, -2))
"""


def zero_sum(num):
    my_map = {}
    count = 0

    for number in num:
        need = -number
        if need in my_map:
            count += 1
        else:
            my_map[number] = my_map.get(number, 0) + 1

    return count


print(zero_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(zero_sum([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))

# time: 37 minutes


# time complexity: O(n)
# space complexity: O(n)
# Follow up: Now assume you can re-use elements in different pairs.
# The elements in a pair must be from different indices,
# but different pairs may use an element from the same index.


def zero_sum_reuse(num):
    my_map = {}
    count = 0

    for number in num:
        my_map[number] = my_map.get(number, 0) + 1

    for number in my_map:
        need = -number
        if need in my_map and number > 0:
            count += my_map[number] * my_map[need]
        elif number == 0:
            count += my_map[0] * (my_map[0] - 1) // 2

    return count


print(zero_sum_reuse([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(zero_sum_reuse([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))

# time: 50min
