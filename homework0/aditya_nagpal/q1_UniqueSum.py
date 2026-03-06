#given array of INTEGERS
# return the SUM of UNIQUE elements in the array

def uniqueSum(arr):
    new_set = set(arr)
    total = 0
    for element in new_set:
        total += element

    return total

print(uniqueSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(uniqueSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))
