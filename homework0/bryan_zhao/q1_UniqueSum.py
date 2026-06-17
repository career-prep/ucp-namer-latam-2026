#Time Complexity: O(n)
#Space Complexity: O(n)

def unique_sum(arr) -> int:
    total = 0
    unique_vals = set(arr)

    for val in unique_vals:
        total += val
    
    return total


test_case1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
#Output: 33

test_case2 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
#Output: 35

print(unique_sum(test_case1))
print(unique_sum(test_case2))

#Time spent on unique_sum: 5 minutes