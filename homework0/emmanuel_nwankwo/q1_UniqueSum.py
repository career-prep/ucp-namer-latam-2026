# Time Complexity: O(n)
# Space Complexity: O(n)

def unique_sum(arr):
    arr_set = set(arr)
    return sum(arr_set)

print(unique_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(unique_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))

# Time spent: 2mins