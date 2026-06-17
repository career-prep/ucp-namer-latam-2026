"""
Use the property of a set to find all unique numbers in the array, then sum them up.
"""

def UniqueSum(arr):
    sum = 0 
    arr = set(arr)

    for i in arr:
        sum += i

    return sum

test = [
    [1, 10, 8, 3, 2, 5, 7, 2, -2, -1],
    [4, 3, 3, 5, 7, 0, 2, 3, 8, 6],
]

for i in test:
    print(UniqueSum(i))

# 10 mins