def MergeKSortedArrays(k, arrays):

    res = []
    for array in arrays:
        for num in array:
            res.append(num)
    
    res.sort()

    return res


# k= 2 
# arrays = [[1, 2, 3, 4, 5], 
#           [1, 3, 5, 7, 9]]
# Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

# k = 4
# arrays = [
#     [1, 4, 8],
#     [2, 6],
#     [0, 3, 7, 10],
#     [5, 9]
# ]
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(MergeKSortedArrays(k, arrays))

# 30