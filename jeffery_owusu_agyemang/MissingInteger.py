# Question 6 (Missing Integer)
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Time spent: 15 mins

def find_missing(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        expected_integer = mid + 1

        if arr[mid] == expected_integer:
            left = mid + 1
        else:
            right = mid - 1
    return left + 1



#Tests

# Q6 Tests
print(find_missing([1, 2, 3, 5, 6], 6))  # 4
print(find_missing([2, 3, 4, 5], 5))     # 1
print(find_missing([1, 2, 3, 4], 5))     # 5
print(find_missing([1], 2))              # 2
