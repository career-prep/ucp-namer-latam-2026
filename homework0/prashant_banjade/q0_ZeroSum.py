# start- 9:20
# Question 1: ZeroSum
# # Given an array of integers, return the number of pairs of integers in the array that sum to 0 assuming you can use the element at each index at most once.

# Examples:
# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1] -Output: 2.  # (Pairs: (1, -1), (2,-2))
# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, - 2, -1]  -Output: 3. # (Pairs: (1, -1), (2, -2), (2,-2))
# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6] -Output: 0
# Input Array: [14, 3, 3, 5, 7, 0, 2, 3, 8, 0] -Output: 1.  # (Pairs: (0, 0))


def zero_sum(arr):
    counter = 0

    d={}

    # lets count the number of value and its count
    for num in arr:
        if num not in d:
            d[num] = 1
        elif (num) in arr:
            d[num] += 1

    # now lets see if that value has the negative pair and compare the count of it
    for val, count in d.items():
        if val < 0 and -(val) in d:
            count += min(d[val], d[-val])
    return count 

print(zero_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(zero_sum([1, 10, 8, -2, 2, 5, 7, 2, - 2, -1]))
print(zero_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))
print(zero_sum([14, 3, 3, 5, 7, 0, 2, 3, 8, 0]))

# used 40 mins till here